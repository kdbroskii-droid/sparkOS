# SparkOS

SparkOS is a lightweight, modular Linux operating system project for x86-64 computers, beginning with the Samsung Chromebook 4 (XE310XBA).

The project is being rebuilt from a clean foundation. The first milestone is a reproducible, bootable Phase 1 image. Desktop features, application runtimes, Spark AI, gaming tools, and advanced graphics work will be added only after the base image boots and hardware is verified.

## Target hardware

- Device: Samsung Chromebook 4, XE310XBA
- CPU: Intel Celeron N4000 (Gemini Lake)
- GPU: Intel UHD Graphics 600
- Memory: 4 GB LPDDR4 (soldered)
- Architecture: x86-64

The device board/HWID must be confirmed on the Chromebook itself before selecting an installation or firmware procedure. Do not infer firmware compatibility from the retail model name alone.

## Project principles

1. Build a real operating system, not a browser-based desktop mockup.
2. Keep the base system small and optional services off until needed.
3. Detect hardware capabilities rather than hardcoding one machine.
4. Treat compatibility as something to test, not promise.
5. Never allow cleanup or AI actions to delete personal data without explicit approval.
6. Keep Spark AI local-first: its inference engine and model library belong to SparkOS. No third-party AI API is required or used by the core assistant.
7. Add features incrementally and keep build/test evidence with each milestone.

## Phase 1

Phase 1 builds a minimal Debian-based live ISO for x86-64 with Linux, firmware, networking, and graphics diagnostics. It is a bootable foundation, not yet the finished desktop OS.

See [Phase 1 foundation](docs/phase-1-foundation.md) and [architecture](docs/architecture.md).

## Build

On a Debian 13 (Trixie) build host with live-build installed:

```bash
sudo apt-get update
sudo apt-get install -y live-build debootstrap ca-certificates xorriso squashfs-tools grub-pc-bin grub-efi-amd64-bin mtools dosfstools syslinux-common isolinux
sudo ./scripts/build-iso.sh
```

The ISO and checksum are written to `out/`.

GitHub Actions runs the same build in a clean Debian container.

## Status

- [x] Repository reset with a recoverable archive branch
- [x] Phase 1 build definition
- [ ] First successful CI ISO build
- [ ] Boot test on generic UEFI virtual machine
- [ ] Chromebook board/HWID confirmation
- [ ] Hardware boot test
- [ ] Desktop environment
- [ ] Native application manager
- [ ] Android runtime evaluation
- [ ] Windows compatibility evaluation
- [ ] Spark AI local runtime and model library
- [ ] Spark Gaming and Spark Neural Graphics

Features are not considered implemented until they have a working implementation and a reproducible test.
