# SparkOS architecture

## Design direction

SparkOS is a Linux distribution with its own native desktop and system services. It is not a web page running in kiosk mode.

The operating system is split into a small base and optional services. The base must boot, provide storage/network access, detect hardware, and recover cleanly without starting Android, Windows compatibility, gaming analysis, or AI workloads.

## Proposed layers

| Layer | Responsibility | Initial status |
|---|---|---|
| Firmware and boot | Chromebook firmware, UEFI boot, Linux kernel, initramfs | Phase 1 |
| Base system | Debian userspace, systemd, filesystem, networking | Phase 1 |
| Hardware service | CPU/GPU/RAM/storage/display/network detection | Phase 1 diagnostics |
| Native desktop | Wayland compositor, shell, SparkBar, launcher, settings | Planned |
| Application manager | Native Linux packages and app metadata | Planned |
| Android runtime | Waydroid evaluation, APK install/launch | Planned; kernel and ABI gated |
| Windows compatibility | Wine/Proton prefixes and app profiles | Planned; per-app testing |
| Spark AI | Local inference service, local model library, permission broker | Planned |
| Spark Storage | Storage analysis and confirmed cleanup operations | Planned |
| Spark Gaming | Game detection, monitoring, reversible tuning | Planned |
| Spark Neural Graphics | Capability detection and supported rendering integrations | Research/planned |

## Spark AI: independent local system

Spark AI is a SparkOS subsystem, not a thin client for another company's AI API.

Its planned components are:

- **Inference engine:** a locally running, replaceable inference backend.
- **Model library:** SparkOS-managed catalogue of locally stored models, model metadata, checksums, versions, and hardware requirements.
- **Model manager:** explicit download, verification, selection, update, and removal.
- **System context service:** read-only, structured information from approved SparkOS services.
- **Action broker:** permission-gated operations with preview and confirmation for consequential changes.
- **User interface:** conversation and command interface, loaded only when requested.

The 4 GB target makes large local models impractical. Phase 1 must not ship a model or keep an inference process resident. Later model choices must be benchmarked on the actual device, and the assistant must explain when a task exceeds local hardware capacity.

No cloud AI provider is required by the core design. Optional remote providers are outside the requested core architecture and are not part of the initial implementation.

## Desktop direction

The future desktop should use native Linux windowing and system APIs. A Wayland compositor is preferred, subject to testing on the Intel UHD 600. The shell, launcher, taskbar, settings, notifications, and quick settings should communicate with system services through documented local interfaces.

Visual effects must have a reduced-effects mode. Blur and translucency are optional and must never be required for usability.

## Resource policy

- Start only essential services.
- Start Android, Wine helpers, Spark AI, and game monitoring on demand.
- Put memory and CPU limits on optional services.
- Keep caches bounded and disposable.
- Avoid persistent writes to removable SD storage unless the user selects it.
- Reserve memory for the desktop and kernel before optional workloads.
- Never kill essential services as a gaming optimisation.

## Compatibility policy

APK and EXE are package formats, not compatibility guarantees. Each runtime must report its architecture, graphics, kernel, and dependency requirements. Every application marked supported must have a reproducible test record.

Spark Neural Graphics may only expose features implemented through supported drivers, APIs, or application integrations. It must not claim to alter arbitrary games or reproduce proprietary console hardware features.
