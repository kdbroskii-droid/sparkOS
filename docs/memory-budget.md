# SparkOS RAM budget

## Priority

Minimise physical RAM consumption. Disk capacity is a secondary concern. The initial hardware target has 4 GB RAM, so every resident component must justify its cost.

## Rules

1. Boot only the kernel and minimum services needed to reach a usable system.
2. Prefer small native components over a browser-based shell or large desktop stack.
3. Start optional components only on demand: Spark AI, Android support, Windows compatibility, indexing, game monitoring, and development tools.
4. Keep caches bounded and release temporary allocations promptly.
5. Share graphics and file buffers when safe; avoid duplicate copies of large assets.
6. Load local AI models on demand and unload them when no longer in use or when memory pressure demands it.
7. Protect essential kernel and base services from optional workloads.
8. Treat swap as an optional safety net, not as a replacement for efficient memory use.
9. Keep logs and persistent writes on storage where practical, while avoiding excessive writes.
10. Measure actual memory use instead of promising untested numbers.

## Required measurements

For each bootable release, record:

- Total physical memory detected.
- Kernel and base-system memory after boot.
- Idle memory after reaching the native desktop.
- Peak memory during common tasks.
- Incremental memory cost of Spark AI, Android support, Windows compatibility, and gaming tools.
- Swap activity and responsiveness under memory pressure.

Include the device, build commit, test method, and raw results. Do not call a target achieved until it has been tested on a reproducible build.
