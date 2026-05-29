#!/bin/bash
set -e

COPR="andersrh/sonicDE"
GIT_URL="https://pc-rytteren.dk/forge/anders/SonicDE-rpmspecs.git"
BRANCH="10_2"
METHOD="rpkg"

# Build order tiers (sequential within tier for dependency safety)
TIER1=(
  sonic-silver-theme
  sonic-frameworks-keybind
  sonic-frameworks-windowsystem
  sonic-keybind-daemon
  sonic-sysguard-library
  sonic-screen-library
  sonic-interface-libraries
  sonic-system-info
  sonic-login-manager
)

TIER2=(
  sonic-screen
  sonic-screenlocker
)

TIER3=(
  sonic-win
)

TIER4=(
  sonic-workspace
)

TIER5=(
  sonic-desktop-interface
)

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
  local -n tier=$1
  local tier_name=$2
  local pids=()

  echo ""
  echo "========================================"
  echo "  $tier_name"
  echo "========================================"

  for pkg in "${tier[@]}"; do
    submit_scm "$pkg" &
    pids+=($!)
  done

  # Wait for all builds in this tier
  for pid in "${pids[@]}"; do
    wait $pid || { echo "FEJL: Bygning fejlede i $tier_name"; exit 1; }
  done
  echo "  $tier_name færdig"
}

usage() {
  echo "Brug: $0 [tier1|tier2|tier3|tier4|tier5|all ...]"
  echo "  tier1   - Byg Tier 1 pakker (uden afhængigheder)"
  echo "  tier2   - Byg Tier 2 pakker"
  echo "  tier3   - Byg Tier 3 pakker"
  echo "  tier4   - Byg Tier 4 pakker"
  echo "  tier5   - Byg Tier 5 pakker"
  echo "  all     - Byg alle tiers (default hvis intet angivet)"
  echo ""
  echo "Eksempler:"
  echo "  $0 tier2         # Kør kun Tier 2"
  echo "  $0 tier1 tier2   # Kør Tier 1 og 2"
  exit 1
}

# Determine which tiers to run
if [ $# -eq 0 ]; then
  set -- all
fi

# Validate args
for arg; do
  case "$arg" in
    tier1|tier2|tier3|tier4|tier5|all) ;;
    *) echo "Ukendt argument: $arg"; usage ;;
  esac
done

echo "Bygger SonicDE pakker i Copr fra git repo"
echo "COPR:   $COPR"
echo "GIT:    $GIT_URL"
echo "Branch: $BRANCH"
echo ""

for arg; do
  case "$arg" in
    tier1) submit_tier TIER1 "Tier 1" ;;
    tier2) submit_tier TIER2 "Tier 2" ;;
    tier3) submit_tier TIER3 "Tier 3" ;;
    tier4) submit_tier TIER4 "Tier 4" ;;
    tier5) submit_tier TIER5 "Tier 5" ;;
    all)
      submit_tier TIER1 "Tier 1"
      submit_tier TIER2 "Tier 2"
      submit_tier TIER3 "Tier 3"
      submit_tier TIER4 "Tier 4"
      submit_tier TIER5 "Tier 5"
      ;;
  esac
done

echo ""
echo "Kørsel færdig."
