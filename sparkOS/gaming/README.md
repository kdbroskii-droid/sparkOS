# SparkOS Game Mode / SparkBoost

Game Mode prioritizes the active game, reduces background activity, and provides bounded RAM/storage caching.

Default limits:
- up to 35% of currently free RAM
- up to 35% of currently free storage
- 512 MB RAM safety reserve
- 8 GB storage safety reserve

Storage is never converted into RAM or GPU memory. It is used only for caches, temporary assets and shader data.
