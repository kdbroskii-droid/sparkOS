#!/bin/sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
OUT="${1:-$ROOT/../../build}"
rm -rf "$OUT"
mkdir -p "$OUT/efi/EFI/BOOT" "$OUT/efi/EFI/Linux" "$OUT/system" "$OUT/recovery"
cp "$ROOT/layout.conf" "$OUT/layout.conf"
cp "$ROOT/../recovery/"*.sh "$OUT/recovery/"
cp "$ROOT/../recovery/"*.py "$OUT/recovery/"
cp "$ROOT/../recovery/recovery.conf" "$OUT/recovery/"
cp "$ROOT/../recovery/systemd-boot-recovery.conf" "$OUT/recovery/"
cat > "$OUT/IMAGE-PLAN.txt" <<'EOF'
SparkOS x86_64 Chromebook image
ESP: bootloader + UKI
SYSTEM: SparkOS root filesystem
RECOVERY: separate verified recovery environment
The final disk image needs a Chromebook-compatible kernel and firmware configuration.
EOF
echo "SparkOS image staging complete: $OUT"
