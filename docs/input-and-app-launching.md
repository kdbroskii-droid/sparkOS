# App launching and keyboard/mouse input

## Scope and honest status

This repository does not yet have a bootable independent kernel, a native window manager, an input driver, or a process manager. Therefore this change implements a small, dependency-free **routing core** and records the default bindings; it does not claim that physical input or app windows already work on a booted SparkOS machine.

The routing core is in `components/shell-core`. It converts normalized key and mouse events into stable shell actions. The eventual kernel/input stack must deliver events to the session manager, and the session manager must implement `ShellActions` using native window/process services.

## Default keyboard bindings

| Shortcut | Action |
|---|---|
| Super + Space | Open app launcher |
| Super + E | Open Files |
| Super + B | Open Browser |
| Super + S | Open Settings |
| Super + I | Open Spark AI on demand |
| Super + T | Open Terminal |
| Super + 1–9 | Open pinned app in that slot |
| Alt + F4 | Close focused window |
| Alt + Tab | Switch windows |
| F11 | Toggle maximize |
| Super + Tab | Task view |
| Super + D | Show desktop |
| Super + Left/Right | Previous/next workspace |
| Super + Q | Quick settings |
| Super + N | Notifications |
| Super + Alt + Left/Right | App navigation back/forward |

## Default mouse bindings

- Left click activates the pointer target.
- Right click opens the target's context menu.
- Mouse Back/Forward navigate history when the focused app supports it.
- Wheel scrolls vertically; Shift + wheel is reserved for horizontal scrolling.
- Middle-click is passed through to the focused application by default.

## App opening model

Apps are opened by stable IDs from `config/apps.toml`, not by running arbitrary command strings from keyboard input. The native app manager resolves an ID to an installed, verified app manifest and asks the process/session manager to launch it. Existing app instances may be focused instead of launching duplicates where the app declares single-instance behaviour. Missing apps should return a visible “not installed” error, not crash the shell.

The launcher should be searchable and lazy-loaded. Pinned slots are configurable. Spark AI and other heavy optional components must start on demand and exit/unload when no longer needed.

## Input path required for actual hardware

1. Device drivers decode keyboard, mouse, touchpad, and USB HID reports.
2. The kernel/input service emits normalized key-down/up, pointer, button, and wheel events.
3. The session manager applies configurable bindings before delivering unconsumed events to the focused application.
4. The compositor routes pointer coordinates and window focus; applications receive ordinary input not consumed by global bindings.

For a minimal-RAM design, keep the binding table in the shell/session process rather than adding a permanent standalone daemon. Support keyboard layout translation, key repeat, key-up events, multiple keyboards, touchpad gestures, accessibility options, and per-user remapping before calling the input stack complete.

## Testing

The Rust routing core has unit tests for app launch dispatch, Alt+F4, unbound key passthrough, and mouse click routing. Run:

```sh
cargo test --manifest-path components/shell-core/Cargo.toml
```

These tests exercise only the routing logic; they do not test hardware drivers, graphical windows, or real app processes.
