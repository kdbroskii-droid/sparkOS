# Installing SparkOS on the Samsung Chromebook 4

## Current status

Do not remove ChromeOS yet. SparkOS does not currently have a bootable independent kernel or a complete desktop, so there is no installable SparkOS image to replace ChromeOS with. The app manifests and Settings files are specifications; they are not a working operating system.

## Safe path from source code to the Chromebook

1. Develop SparkOS on a separate computer or in a virtual machine first.
2. Build the independent kernel and minimal boot image, and test boot, memory management, keyboard input, display output, and storage in an emulator.
3. Add the native desktop/session manager and app runtime; test the app-launch routes and Settings persistence.
4. Produce a reproducible USB image and verify its checksum.
5. Identify the Chromebook's exact board/HWID from its Recovery/Developer Mode screen or `chrome://system`. The retail model name alone is not enough to select firmware.
6. Check the exact board against the official device-support table and read the firmware project's full instructions before making firmware changes.
7. Keep a ChromeOS recovery USB and a verified stock-firmware backup on separate storage. Back up personal files too.
8. Test the SparkOS image on supported hardware without erasing the existing installation first, where the verified firmware path permits it.
9. Only after SparkOS boots reliably and the recovery path is understood should you decide whether to replace ChromeOS. Firmware flashing can brick the Chromebook; get an experienced adult's help and do not open the device or change write protection based on guesswork.

## Important Chromebook facts

- Entering Developer Mode erases local Chromebook data.
- Replacing stock firmware with UEFI Full ROM can remove ChromeOS and ChromeOS Recovery Mode, and a firmware mistake can leave the device unable to boot.
- Firmware availability does not guarantee that Wi-Fi, audio, graphics, suspend, keyboard, or other hardware will work in a new OS.
- Do not run firmware-flashing commands copied from a chat before confirming the exact board, firmware support, backup, and recovery plan.

## References

- Google Chromebook recovery: https://support.google.com/chromebook/answer/1080595
- ChromiumOS Developer Mode information: https://www.chromium.org/chromium-os/developer-library/guides/device/developer-mode/
- MrChromebox supported-device list: https://docs.mrchromebox.tech/docs/supported-devices
- MrChromebox firmware flashing warnings and procedure: https://docs.mrchromebox.tech/docs/firmware/flashing-firmware.html

These links explain ChromeOS recovery and firmware concepts. They do not mean SparkOS is currently ready to install.