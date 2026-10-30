# SparkOS Settings app

## Status

This file specifies the planned Settings app information architecture. It is not yet a running GUI: the independent kernel, native compositor/window manager, session manager, and app runtime are not implemented.

## Layout

- Left navigation rail with searchable Settings categories.
- Main panel with a title, short description, and controls for the selected category.
- Search field that filters category names and settings.
- Changes should apply immediately where safe and persist per user.
- Show unavailable controls as disabled with a reason; do not display fake success states.
- Keyboard navigation and touchpad/mouse operation are required.
- Use a low-memory native UI; do not make the desktop or Settings shell a web page.

## Categories

The source of truth is `config/settings-sections.toml`. It covers Appearance, Display, Keyboard, Mouse & Touchpad, Apps, Network (Wi-Fi only; no Ethernet section), Sound, Bluetooth, Power, Storage, Privacy & Security, Users, Date & Time, Accessibility, Spark AI, System, and Developer.

## Chromebook input

Treat the physical Search/Launcher key as the SparkOS launcher modifier by default, but verify its scancode on the Samsung Chromebook 4 XE310XBA before finalizing the input driver. Provide a remapping option so users can change the behaviour.

## Safety and persistence

- Validate settings before applying them.
- Keep a recoverable previous configuration when changing boot, display, keyboard, or networking settings.
- Require confirmation for destructive actions such as removing an account or resetting settings.
- Never include a control that erases ChromeOS or rewrites firmware until a bootable SparkOS image and a tested recovery path exist.
- Mark unfinished features as unavailable instead of pretending they work.

## Implementation sequence

1. Build the native Settings window and category navigation.
2. Add a typed settings model with validation and a versioned on-disk format.
3. Connect settings to keyboard/input, display, Wi-Fi, sound, and power services as those services become real.
4. Add persistence and tests for loading, saving, invalid values, and migration.
5. Verify memory use and keyboard/touchpad accessibility on the target Chromebook.