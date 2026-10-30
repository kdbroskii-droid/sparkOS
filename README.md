# SparkOS

SparkOS is an independent operating-system project targeting x86-64 computers, beginning with the Samsung Chromebook 4 (XE310XBA). The long-term target is a SparkOS-owned kernel and native system stack, not a Debian-based distribution.

The repository is being rebuilt incrementally. The current Phase 1 Debian live-build configuration is temporary build scaffolding and does **not** meet the independent-kernel goal. It must not be presented as the finished SparkOS architecture. The next foundation milestone is a minimal independently built kernel that boots and prints a SparkOS startup screen; the old SparkOS logo and startup animation should be preserved from the archived source where possible.

## Target hardware

- Device: Samsung Chromebook 4, XE310XBA
- CPU: Intel Celeron N4000 (Gemini Lake)
- GPU: Intel UHD Graphics 600
- Memory: 4 GB LPDDR4 (soldered)
- Architecture: x86-64

Confirm the device board/HWID on the Chromebook itself before selecting an installation or firmware procedure. Do not infer firmware compatibility from the retail model name alone.

## Core principles

1. Build an independent OS, kernel-first; do not make Debian the product's base.
2. Prioritise minimal RAM consumption over saving disk space.
3. Start only essential services; start optional components on demand.
4. Keep the native desktop lightweight and avoid a browser-based desktop.
5. Spark AI must have its own local inference engine and model library, not just an API wrapper.
6. Detect hardware capabilities rather than hardcoding one machine.
7. Treat compatibility as something to test, not promise.
8. Never delete personal data without explicit approval.
9. Features are not complete until a reproducible test supports the claim.

## RAM-first design

The main target has 4 GB of physical RAM. RAM efficiency is a first-class requirement; disk capacity is secondary.

- Keep the kernel, init path, and base services small.
- Avoid launching a full service manager or background daemon for every feature unless the design proves it necessary.
- Load drivers and services only when required, where technically safe.
- Use bounded caches and release temporary buffers promptly.
- Keep AI, Android compatibility, Windows compatibility, game tools, and indexing stopped until requested.
- Load AI models on demand; unload them when the user exits Spark AI or memory pressure requires it.
- Avoid duplicated texture, image, and model buffers; prefer shared buffers where supported.
- Provide memory-pressure reporting and graceful low-memory behaviour.
- Treat swap as a safety mechanism, not a substitute for RAM; make it configurable and avoid constant swapping.
- Measure idle boot RAM, desktop idle RAM, and each optional feature separately on real hardware.

No RAM figures are claimed until measured on a booted build. The target is to minimise idle memory while retaining stability and usable graphics.

## Development milestones

1. Independent bootable kernel and SparkOS boot screen.
2. Memory allocator, interrupt handling, timers, serial/debug output, and basic hardware discovery.
3. RAM-first base services, storage, and networking.
4. Lightweight native graphical stack.
5. Spark AI local inference engine and model library.
6. Android and Windows compatibility research and implementation.
7. GPU acceleration, gaming support, and optional graphics features.

Android, Windows apps, local AI inference, and advanced GPU features are not implemented merely because they appear on this roadmap.

## Current repository status

The current Phase 1 build files still describe a Debian-based Linux image and therefore do not yet satisfy the independent-kernel requirement. They are scaffolding to be replaced, not the intended final design. No successful independent-kernel boot or memory benchmark is claimed yet.

See [architecture](docs/architecture.md) and [RAM budget](docs/memory-budget.md).


## First app and desktop specifications

The initial app IDs are Files, Google Chrome, Settings, and Terminal. Their registry is `config/apps.toml`; per-app contracts are under `apps/`. The planned Settings categories are in `config/settings-sections.toml`, with design notes in [docs/settings-app.md](docs/settings-app.md). Chromebook key mappings and app routing are documented in [docs/input-and-app-launching.md](docs/input-and-app-launching.md). The safe install sequence is in [docs/chromebook-installation-plan.md](docs/chromebook-installation-plan.md).

**Status warning:** app manifests, settings definitions, and shortcut routing are scaffolding only. The native apps, bootable independent kernel, desktop/session manager, and actual install image are not yet implemented. Do not erase ChromeOS based on this repository's current state.
