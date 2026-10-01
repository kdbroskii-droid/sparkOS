#!/bin/sh
set -eu
ROOT=${SPARK_RECOVERY_ROOT:-/run/sparkos-recovery}
mkdir -p "$ROOT"
say(){ printf '%s\n' "$*"; }
verify(){ [ -x "$ROOT/verify.sh" ] && "$ROOT/verify.sh"; }
factory_reset(){
 root=${SPARK_OS_ROOT:-/sysroot}; [ -d "$root" ] || { say "SparkOS root unavailable";return 1; }
 say "FACTORY_RESET_START"
 [ -d "$root/home" ] && find "$root/home" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
 [ -d "$root/var/lib/sparkos" ] && find "$root/var/lib/sparkos" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
 say "FACTORY_RESET_PROGRESS 100";say "FACTORY_RESET_DONE"
}
case "${1:-menu}" in
 verify)verify;; reset)factory_reset;; usb)say "USB recovery selected";; storage)say "Storage recovery selected";; web)say "Web recovery selected";;
 menu)say "SparkOS Recovery";say "1) Get OS from USB";say "2) Get OS from Storage";say "3) Get OS from Web";say "4) Verify system";say "5) Factory reset";;
 *)say "Usage: recovery.sh [menu|verify|usb|storage|web|reset]";exit 2;;
esac
