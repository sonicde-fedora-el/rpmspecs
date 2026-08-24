#!/usr/bin/env bash
# Installer for the SonicDE RPM macros without building the package.  Used by
# CI so specs referring to macros like %majmin_ver_kf6 parse the same way they
# do on a system with sonic-rpm-macros installed.
set -euo pipefail

cd "$(dirname "$0")/.."

spec=sonic-rpm-macros/sonic-rpm-macros.spec
frameworks=$(rpmspec -q --srpm --queryformat '%{version}\n' "$spec")
plasma=$(sed -n 's/^%global sonicde_plasma_version \(.*\)$/\1/p' "$spec")
target=$(rpm --eval '%{_rpmconfigdir}')/macros.d/macros.kf6

install -Dpm 644 sonic-rpm-macros/macros.kf6 "$target"
sed -i \
  -e "s|@@kf6_VERSION@@|$frameworks|g" \
  -e "s|@@sonicde_frameworks_VERSION@@|$frameworks|g" \
  -e "s|@@sonicde_plasma_VERSION@@|$plasma|g" \
  "$target"

echo "installed $target (frameworks $frameworks, plasma $plasma)"
