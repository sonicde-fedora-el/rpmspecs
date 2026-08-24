#!/bin/bash
set -e

COPR="${COPR:-@SonicDE/SonicDE-EL10}"
GIT_URL="${GIT_URL:-https://pc-rytteren.dk/forge/anders/SonicDE-rpmspecs.git}"
BRANCH="${BRANCH:-master}"
METHOD="${METHOD:-rpkg}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ORDER_FILE="$SCRIPT_DIR/build-order.txt"

# All tier names present in build-order.txt, in order.
tier_names() {
  sed -n 's/^\[\(tier[0-9]\+\)\]$/\1/p' "$ORDER_FILE"
}

# Packages of a single tier.
tier_packages() {
  sed -n "/^\[$1\]$/,/^\[/p" "$ORDER_FILE" |
    grep -v '^\[' | grep -v '^#' | grep -v '^$'
}

# Submit SCM build to Copr (blocks until completion by default)
submit_scm() {
  local pkg=$1
  echo "=== Bygger $pkg i Copr (SCM) ==="
  copr-cli buildscm "$COPR" \
    --clone-url "$GIT_URL" \
    --commit "$BRANCH" \
    --subdir "$pkg" \
    --spec "$pkg.spec" \
    --method "$METHOD"
}

# Submit tier in parallel
submit_tier() {
  local tier=$1
  local pids=()

  echo ""
  echo "========================================"
  echo "  $tier"
  echo "========================================"

  for pkg in $(tier_packages "$tier"); do
    submit_scm "$pkg" &
    pids+=($!)
  done

  for pid in "${pids[@]}"; do
    wait $pid || { echo "FEJL: Bygning fejlede i $tier"; exit 1; }
  done
  echo "  $tier færdig"
}

usage() {
  echo "Brug: $0 [tierN ...|all]"
  echo "  tierN   - Byg pakkerne i den angivne tier fra build-order.txt"
  echo "  all     - Byg alle tiers i rækkefølge (default hvis intet angivet)"
  echo ""
  echo "Tiers i $ORDER_FILE:"
  for t in $(tier_names); do
    echo "  $t ($(tier_packages "$t" | wc -l) pakker)"
  done
  echo ""
  echo "Miljøvariabler: COPR, GIT_URL, BRANCH, METHOD"
  exit 1
}

if [ $# -eq 0 ]; then
  set -- all
fi

for arg; do
  case "$arg" in
    all) ;;
    tier[0-9]*)
      tier_names | grep -qx "$arg" || { echo "Ukendt tier: $arg"; usage; } ;;
    *) echo "Ukendt argument: $arg"; usage ;;
  esac
done

echo "Bygger SonicDE pakker i Copr fra git repo"
echo "COPR:   $COPR"
echo "GIT:    $GIT_URL"
echo "Branch: $BRANCH"
echo ""

for arg; do
  if [ "$arg" = all ]; then
    for t in $(tier_names); do
      submit_tier "$t"
    done
  else
    submit_tier "$arg"
  fi
done

echo ""
echo "Kørsel færdig."
