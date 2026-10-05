# SparkOS Game Mode / SparkBoost

SparkBoost automatically activates for detected games, while still allowing a manual Game Mode toggle.

## Performance allocation

- Up to **35% of currently available RAM** for useful caching/prioritization.
- Up to **35% of currently free storage** for the normal game cache.
- A separate **15% predictable-data cache** for game data that is known to be reusable and stable.
- 512 MB RAM safety reserve.
- 8 GB storage safety reserve.

The 15% predictable-data cache is separate from the normal 35% cache, but the safety reserve and available-space checks always win. SparkOS must never fill storage just because a percentage is configured.

## Predictable-data caching

Some games repeatedly use the same assets, maps, shaders, or other data. SparkOS can keep copies of **game-provided or user-approved cacheable data** in a persistent predictable-data cache.

The flow is:

**storage → RAM/page cache → GPU/CPU → rendered frame**

When a game changes data, SparkOS does not guess that a change is safe to save. Only game-provided, explicitly cacheable data or user-approved persistent state is stored.

This means SparkOS cannot automatically reconstruct or save Fortnite's internal map/destruction state unless the game itself exposes that data. The OS cannot safely invent that information.

Linux already caches file data in memory and can reclaim that cache when memory is needed; SparkBoost adds bounded, persistent storage caching on top of normal OS caching. citeturn0search5turn0search8

## What SparkBoost does not do

- It does not turn storage into RAM.
- It does not turn storage into VRAM.
- It does not render graphics on the storage device.
- It does not modify game files.
- It does not bypass anti-cheat.
- It does not assume that every game has deterministic assets.

The GPU still performs rendering. The cache only helps make reusable data available with less repeated disk I/O.
