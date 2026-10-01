#!/bin/sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
for app in files terminal settings app-store; do python3 -m py_compile "$ROOT/$app/main.py"; done
python3 -m py_compile "$ROOT/../system/network/wifi.py"
python3 -m py_compile "$ROOT/../system/network/bluetooth.py"
python3 -m py_compile "$ROOT/../recovery/recovery-state.py"
sh -n "$ROOT/../recovery/recovery.sh"
sh -n "$ROOT/../recovery/verify.sh"
echo "SparkOS application, wireless and recovery sources passed validation."
