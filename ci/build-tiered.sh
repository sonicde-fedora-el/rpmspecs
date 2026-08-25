#!/usr/bin/env bash
# Build SonicDE packages in tier order inside a mock chroot.
#
# Usage: ci/build-tiered.sh <build-plan.json>
#
# After each package is built, its RPMs are installed into the mock chroot
# so they're available as build dependencies for subsequent tiers.
set -euo pipefail

PLAN_FILE="${1:?usage: build-tiered.sh <plan.json>}"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCES_DIR="${HOME}/rpmbuild/SOURCES"
RESULTS_DIR="${HOME}/mock-results"
MOCK_ROOT="${MOCK_ROOT:-sonicde}"

# Forgejo upload config (optional - if not set, upload is skipped)
FORGEJO_URL="${FORGEJO_URL:-}"
FORGEJO_OWNER="${FORGEJO_OWNER:-}"
FORGEJO_TOKEN="${FORGEJO_TOKEN:-}"

upload_rpms() {
    local pkg=$1
    local result_dir=$2

    if [ -z "$FORGEJO_URL" ] || [ -z "$FORGEJO_OWNER" ] || [ -z "$FORGEJO_TOKEN" ]; then
        return 0
    fi

    for rpm in $(find "$result_dir" -name '*.rpm' ! -name '*.src.rpm'); do
        local filename=$(basename "$rpm")
        echo "  Uploading $filename to Forgejo..."
        if curl --fail-with-body --silent --show-error \
            --user "${FORGEJO_OWNER}:${FORGEJO_TOKEN}" \
            --upload-file "$rpm" \
            "${FORGEJO_URL}/api/packages/${FORGEJO_OWNER}/rpm/upload"; then
            echo "  Uploaded: $filename"
        else
            echo "  WARNING: upload failed for $filename"
        fi
    done
}

mkdir -p "$RESULTS_DIR" "$SOURCES_DIR"

TOTAL=$(python3 -c "import json; print(json.load(open('$PLAN_FILE'))['total'])")
BUILT=0
FAILED=()

NUM_TIERS=$(python3 -c "import json; print(len(json.load(open('$PLAN_FILE'))['tiers']))")

for tier_idx in $(seq 0 $((NUM_TIERS - 1))); do
    TIER_NUM=$(python3 -c "import json; print(json.load(open('$PLAN_FILE'))['tiers'][$tier_idx]['tier'])")
    PACKAGES=$(python3 -c "import json; print('\n'.join(json.load(open('$PLAN_FILE'))['tiers'][$tier_idx]['packages']))")
    PKG_COUNT=$(echo "$PACKAGES" | wc -l)

    echo ""
    echo "========================================"
    echo "  Tier ${TIER_NUM}: ${PKG_COUNT} packages"
    echo "========================================"

    for pkg in $PACKAGES; do
        BUILT=$((BUILT + 1))
        echo ""
        echo "[${BUILT}/${TOTAL}] Building ${pkg}..."

        spec_dir="${REPO_DIR}/${pkg}"
        spec="${spec_dir}/${pkg}.spec"

        if [ ! -f "$spec" ]; then
            echo "  SKIP: spec not found: ${spec}"
            continue
        fi

        # Copy local source files (patches, configs, etc.)
        find "$spec_dir" -maxdepth 1 -type f ! -name '*.spec' \
            -exec cp -p {} "$SOURCES_DIR/" \;

        # Download URL sources
        spectool -g -C "$SOURCES_DIR" "$spec" 2>&1 | tail -2 || true

        # Build SRPM
        rpmbuild -bs \
            --define "_topdir ${HOME}/rpmbuild" \
            --define "_disable_source_fetch 0" \
            "$spec" 2>&1 | tail -3

        srpm_name=$(rpmspec -q --srpm \
            --queryformat '%{NAME}-%{VERSION}-%{RELEASE}.src.rpm' "$spec")
        srpm_path="${HOME}/rpmbuild/SRPMS/${srpm_name}"

        # Build with mock
        pkg_result_dir="${RESULTS_DIR}/${pkg}"
        rm -rf "$pkg_result_dir"
        mkdir -p "$pkg_result_dir"

        if mock --root "$MOCK_ROOT" \
                --resultdir "$pkg_result_dir" \
                --no-clean --rebuild "$srpm_path" 2>&1 | tail -10; then
            echo "  OK: ${pkg}"

            # Install the built RPMs into the mock chroot so later tiers
            # can use them as build dependencies.
            echo "  Installing ${pkg} RPMs into chroot..."
            mock --root "$MOCK_ROOT" --no-clean --install \
                $(find "$pkg_result_dir" -name '*.rpm' ! -name '*.src.rpm') \
                2>&1 | tail -3 || echo "  WARNING: could not install ${pkg} into chroot"

            # Upload RPMs to Forgejo immediately so they're available even
            # if a later package fails the build.
            upload_rpms "$pkg" "$pkg_result_dir"
        else
            echo "  FAILED: ${pkg}"
            FAILED+=("$pkg")
        fi

        # Clean SRPM to save disk space
        rm -f "$srpm_path"
    done
done

echo ""
echo "========================================"
echo "  Summary: $((TOTAL - ${#FAILED[@]}))/${TOTAL} succeeded"
if [ ${#FAILED[@]} -gt 0 ]; then
    echo "  Failed: ${FAILED[*]}"
    exit 1
fi
echo "========================================"
