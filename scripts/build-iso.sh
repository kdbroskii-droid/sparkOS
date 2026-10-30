#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v lb >/dev/null 2>&1; then
  echo "live-build is required. Install it with: sudo apt-get install live-build" >&2
  exit 1
fi

if [[ ! -f config/package-lists/sparkos.list.chroot ]]; then
  echo "Missing SparkOS package list." >&2
  exit 1
fi

lb config \
  --mode debian \
  --system live \
  --distribution trixie \
  --architectures amd64 \
  --binary-images iso-hybrid \
  --bootloaders "grub-pc grub-efi" \
  --firmware-binary true \
  --firmware-chroot true \
  --apt-recommends false \
  --archive-areas "main contrib non-free non-free-firmware" \
  --bootappend-live "boot=live components quiet" \
  --debian-installer false \
  --checksums sha256

lb build

OUTPUT_DIR="$ROOT_DIR/out"
if [[ -n "${SPARKOS_OUTPUT_DIR:-}" ]]; then
  OUTPUT_DIR="$SPARKOS_OUTPUT_DIR"
fi
mkdir -p "$OUTPUT_DIR"

ISO_SOURCE="$ROOT_DIR/live-image-amd64.hybrid.iso"
if [[ ! -s "$ISO_SOURCE" ]]; then
  echo "Build completed without the expected ISO: $ISO_SOURCE" >&2
  exit 1
fi

cp "$ISO_SOURCE" "$OUTPUT_DIR/SparkOS-amd64-phase1.iso"
(
  cd "$OUTPUT_DIR"
  sha256sum SparkOS-amd64-phase1.iso > SparkOS-amd64-phase1.iso.sha256
)

echo "SparkOS Phase 1 image:"
ls -lh "$OUTPUT_DIR/SparkOS-amd64-phase1.iso" "$OUTPUT_DIR/SparkOS-amd64-phase1.iso.sha256"
