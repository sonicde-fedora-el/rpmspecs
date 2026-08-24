#!/bin/bash
# Parse every spec in the repository and check that all packages listed in
# build-order.txt have a spec (and vice versa).
set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

fail=0

for spec in */*.spec; do
  dir=${spec%%/*}
  base=$(basename "$spec" .spec)
  if [ "$dir" != "$base" ]; then
    echo "FEJL: $spec ligger ikke i mappen $base"
    fail=1
    continue
  fi
  if ! out=$(rpmspec -q --srpm --queryformat '%{name} %{version}-%{release}\n' "$spec" 2>&1); then
    echo "FEJL: kan ikke parse $spec"
    echo "$out"
    fail=1
    continue
  fi
  echo "$out"
  if warn=$(rpmspec -P "$spec" 2>&1 >/dev/null) && [ -n "$warn" ]; then
    echo "ADVARSEL i $spec:"
    echo "$warn"
  fi
done

ordered=$(grep -v '^\[' build-order.txt | grep -v '^#' | grep -v '^$' | sort)
present=$(for spec in */*.spec; do basename "$spec" .spec; done | sort)

missing=$(comm -13 <(echo "$ordered") <(echo "$present"))
extra=$(comm -23 <(echo "$ordered") <(echo "$present"))

if [ -n "$missing" ]; then
  echo "FEJL: pakker uden plads i build-order.txt:"
  echo "$missing"
  fail=1
fi
if [ -n "$extra" ]; then
  echo "FEJL: build-order.txt nævner pakker uden spec:"
  echo "$extra"
  fail=1
fi

exit $fail
