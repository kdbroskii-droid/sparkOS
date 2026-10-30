# Phase 1 — bootable foundation

## Objective

Produce a reproducible x86-64 Debian 13 (Trixie) live ISO with a generic Linux kernel, firmware packages, networking, and hardware/graphics diagnostic tools.

This phase deliberately does not install a desktop shell, Android container, Wine/Proton, AI model, or gaming daemon. Those services would make early boot failures harder to isolate and waste resources on the 4 GB target.

## Base image

- Debian 13 (Trixie)
- amd64
- hybrid ISO image
- GRUB BIOS and UEFI boot support in the ISO
- Linux kernel from Debian
- non-free firmware enabled for supported hardware
- NetworkManager
- Mesa/OpenGL/Vulkan/VA-API diagnostic tools

A generic UEFI ISO build is not proof that the Chromebook can boot it. Chromebook firmware mode and board support must be checked separately.

## Target Chromebook checks

The Samsung Chromebook 4 family is listed as BLUEBIRD by the MrChromebox supported-device table. The actual board name must be read from the device's HWID in ChromeOS Recovery/Developer Mode or `chrome://system` before any firmware-specific instructions are followed.

Do not flash firmware as part of the ISO build. Firmware changes are a separate, device-specific decision and require a verified board identity, a firmware backup, and a recovery plan.

## First validation sequence

1. Build the ISO in GitHub Actions.
2. Verify the SHA-256 checksum.
3. Boot the ISO in a generic UEFI virtual machine.
4. Confirm the live system reaches a login/console without kernel panic.
5. Confirm the kernel, CPU, memory, PCI, USB, storage, and network devices are detected.
6. Confirm Mesa and VA-API diagnostic tools run and report actual capabilities.
7. Confirm shutdown and reboot.
8. Only after generic boot passes, confirm the Chromebook HWID and evaluate a non-destructive boot test.

## Success criteria

Phase 1 is complete only when a CI artifact exists, its checksum verifies, and a documented boot test succeeds. Chromebook support remains unverified until tested on the actual device.

## Known limitations

- No graphical desktop yet.
- No APK or EXE runtime yet.
- No local AI model yet.
- No gaming optimiser yet.
- No neural upscaling, frame generation, or neural lighting claim.
- Hardware-specific suspend, audio, touchpad, Wi-Fi, and power management still require device testing.
