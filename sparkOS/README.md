# SparkOS Real System

This is the production implementation of SparkOS.

The `html/` folder is only a disposable browser-test area. Production code in this folder is intentionally separated from those prototypes.

## Rule

HTML prototypes may be copied into this implementation when they are approved, but deleting `html/` must never remove or alter the real SparkOS system.


## New features

### SparkBoost
- Automatic game detection.
- Up to 35% of available RAM for bounded caching/prioritization.
- Up to 35% of free storage for the normal game cache.
- A separate 15% predictable-data cache for reusable, stable game data.
- Safety reserves prevent the cache from consuming all RAM or storage.

### Second PCs
- Create an isolated second virtual PC with QEMU/KVM.
- Separate virtual RAM, CPU allocation, disk, and network.
- SparkLink is the planned communication layer between the two PCs.
- File sharing, clipboard sharing, discovery, and remote display are opt-in.
