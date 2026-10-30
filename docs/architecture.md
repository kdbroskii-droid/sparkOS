# SparkOS architecture

## Direction

SparkOS is intended to be an independent operating system with its own kernel and native system stack. Debian or another general-purpose Linux distribution must not be the product's base. The current Debian live-build files are temporary scaffolding and must be replaced; they are not proof of an independent OS.

The first real milestone is a minimal kernel that boots in a virtual machine, emits diagnostic output, and displays the SparkOS logo/startup sequence when the graphics path is ready. Preserve the existing logo and startup animation from the archived branch if their source assets can be recovered and licensed for reuse.

## Layer plan

| Layer | Responsibility | Status |
|---|---|---|
| Boot | Firmware handoff, bootloader, kernel entry, diagnostics | Planned |
| Kernel | Memory management, interrupts, timers, scheduler, drivers, system calls | Not implemented |
| Base services | Storage, process/service lifecycle, networking, device discovery | Planned |
| Native desktop | Lightweight compositor, shell, launcher, settings | Planned |
| Application manager | Native application packaging and lifecycle | Planned |
| Android compatibility | Android runtime and ABI/graphics integration | Research/planned |
| Windows compatibility | App compatibility layer and per-app profiles | Research/planned |
| Spark AI | Local inference engine, model library, permission broker | Planned |
| Spark Gaming | Game detection and reversible performance settings | Planned |
| Spark Neural Graphics | Supported GPU/graphics APIs and tested integrations | Research/planned |

## RAM-first policy

SparkOS targets a 4 GB RAM Chromebook, and memory usage takes priority over reducing disk usage.

- Minimise resident kernel and base-system memory without compromising correctness.
- Avoid unnecessary background daemons and duplicate services.
- Make optional subsystems demand-started and stoppable.
- Bound caches; free temporary allocations and graphics buffers promptly.
- Use shared memory/buffers where safe and supported.
- Load AI models only on demand and unload them when idle or under memory pressure.
- Keep indexing, telemetry, update scans, game monitoring, Android, and Windows helpers off unless explicitly needed.
- Avoid memory overcommit assumptions that can cause system-wide failure.
- Design clear low-memory behaviour and protect critical kernel/base services.
- Swap may be offered as a configurable fallback, but must not be used to hide poor RAM use; excessive swap can make the device feel unusably slow.
- Measure memory at boot, at idle desktop, and with each optional subsystem enabled. Record both resident memory and peak memory.
- Do not publish a RAM target as achieved until it has been measured on a reproducible build.

Disk space is secondary: larger optional packages, model downloads, logs, and caches can live on storage if that reduces resident memory, provided the system remains responsive and storage writes are controlled.

## Spark AI

Spark AI is a first-party local subsystem, not merely a client for an external AI API.

Planned components:

- Local inference engine with a documented internal interface.
- SparkOS-managed model library with model metadata, architecture requirements, checksums, and version tracking.
- Model manager for explicit installation, verification, selection, update, and removal.
- Approved system-context interface.
- Permission broker for actions that change system state.
- UI started only when requested.

Do not ship a large model by default. Benchmark small models on target hardware, load models on demand, and explain when local hardware cannot handle a task. No model or inference capability is considered implemented until it runs locally and has tests.

## Logo and startup

Recover the existing SparkOS logo and startup assets from the archived branch before creating replacements. The boot sequence should be lightweight, avoid starting a full graphical stack just to show branding, and fall back to readable diagnostic output if graphics are unavailable.

## Compatibility

APK and EXE are formats, not compatibility guarantees. Each runtime requires explicit architecture, driver, kernel, and dependency support. Mark applications as supported only when there is a reproducible test.

## Build integrity

The current Debian-based live-build configuration does not meet the independent-kernel goal. Do not label its ISO as the finished independent SparkOS. Replace that path with a documented kernel build and boot test before claiming the core OS is operational.
