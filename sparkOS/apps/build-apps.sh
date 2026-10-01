#!/bin/sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
for app in files terminal settings app-store; do
  python3 -m py_compile "$ROOT/$app/main.py"
done
echo "SparkOS application sources passed syntax checks."
