#!/bin/bash
# Build every package of one tier from build-order.txt for a single mock chroot
# and upload the resulting RPMs to the Forgejo package registry.
#
# Usage: ci/build-tier.sh <tier> <mock-config>
#
# Environment:
#   FORGEJO_URL, FORGEJO_OWNER, FORGEJO_TOKEN  upload target (upload is skipped
#                                              when FORGEJO_TOKEN is empty)
set -euo pipefail

TIER=${1:?tier name, e.g. tier1}
MOCK_CONFIG=${2:?mock config, e.g. alma+epel-10-x86_64}

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ORDER_FILE="$REPO_DIR/build-order.txt"
RESULT_DIR="${RESULT_DIR:-$HOME/mock-results}"

packages() {
  sed -n "/^\[$TIER\]$/,/^\[/p" "$ORDER_FILE" |
    grep -v '^\[' | grep -v '^#' | grep -v '^$'
}

write_mock_config() {
  cat > /etc/mock/sonicde.cfg <<MOCKEOF
include('/etc/mock/${MOCK_CONFIG}.cfg')
config_opts['root'] = 'sonicde-${MOCK_CONFIG}'
config_opts['yum.conf'] += """
[sonicde-rpm]
name=SonicDE RPM
baseurl=${SONICDE_REPO_URL:-https://pc-rytteren.dk/forge/api/packages/anders/rpm}
enabled=1
gpgcheck=0

[xlibre-xserver]
name=Copr xlibre-xserver
baseurl=${XLIBRE_REPO_URL:-https://download.copr.fedorainfracloud.org/results/@xlibre/xlibre-xserver/rhel+epel-10-\$basearch/}
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/@xlibre/xlibre-xserver/pubkey.gpg
repo_gpgcheck=0
enabled=1
"""
MOCKEOF
}

upload() {
  local rpm=$1
  if [ -z "${FORGEJO_TOKEN:-}" ]; then
    echo "  (springer upload over: FORGEJO_TOKEN ikke sat)"
    return 0
  fi
  curl --fail-with-body --silent --show-error \
    --user "${FORGEJO_OWNER}:${FORGEJO_TOKEN}" \
    --upload-file "$rpm" \
    "${FORGEJO_URL}/api/packages/${FORGEJO_OWNER}/rpm/upload"
}

rpmdev-setuptree
write_mock_config
mock --root sonicde --init

for pkg in $(packages); do
  spec="$REPO_DIR/$pkg/$pkg.spec"
  echo "=== $pkg ($MOCK_CONFIG) ==="

  find "$REPO_DIR/$pkg" -maxdepth 1 -type f ! -name '*.spec' \
    -exec cp -p {} "$HOME/rpmbuild/SOURCES/" \;
  ( cd "$REPO_DIR/$pkg" && spectool -g -C "$HOME/rpmbuild/SOURCES/" "$pkg.spec" )
  rpmbuild -bs \
    --define "_topdir $HOME/rpmbuild" \
    --define "_disable_source_fetch 0" \
    "$spec"
  srpm="$HOME/rpmbuild/SRPMS/$(rpmspec -q --srpm \
    --queryformat '%{NAME}-%{VERSION}-%{RELEASE}.src.rpm' "$spec")"

  rm -rf "$RESULT_DIR/$pkg"
  mock --root sonicde --resultdir "$RESULT_DIR/$pkg" --no-clean --rebuild "$srpm"

  find "$RESULT_DIR/$pkg" -name '*.rpm' ! -name '*.src.rpm' | while read -r rpm; do
    echo "  uploader $(basename "$rpm")"
    upload "$rpm"
  done
done
