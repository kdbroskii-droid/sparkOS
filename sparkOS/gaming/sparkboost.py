#!/usr/bin/env python3
import hashlib
import json
import shutil
import sys
from pathlib import Path

CONFIG = Path("/etc/sparkos/gaming.json")
CACHE_ROOT = Path("/var/cache/sparkos/game")
PREDICTABLE_ROOT = CACHE_ROOT / "predictable"

DEFAULT = {
    "enabled": False,
    "max_free_ram_fraction": 0.35,
    "max_free_storage_fraction": 0.35,
    "predictable_storage_fraction": 0.15,
    "ram_reserve_mb": 512,
    "storage_reserve_gb": 8,
    "background_services": "reduce",
}

def load():
    try:
        return {**DEFAULT, **json.loads(CONFIG.read_text())}
    except Exception:
        return DEFAULT.copy()

def stats():
    ram = 0
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):
            ram = int(line.split()[1]) * 1024
            break
    d = shutil.disk_usage("/")
    return {"free_ram_bytes": ram, "free_storage_bytes": d.free}

def plan():
    c = load()
    s = stats()

    ram_cap = max(0, s["free_ram_bytes"] - c["ram_reserve_mb"] * 1024**2)
    ram_cache = min(
        int(s["free_ram_bytes"] * c["max_free_ram_fraction"]),
        ram_cap,
    )

    storage_cap = max(
        0,
        s["free_storage_bytes"] - c["storage_reserve_gb"] * 1024**3,
    )

    general_cache = min(
        int(s["free_storage_bytes"] * c["max_free_storage_fraction"]),
        storage_cap,
    )

    # A separate bounded cache for data that a game declares as predictable/
    # reusable. This is not GPU memory and does not render by itself.
    predictable_cache = min(
        int(s["free_storage_bytes"] * c["predictable_storage_fraction"]),
        max(0, storage_cap - general_cache),
    )

    return {
        "enabled": c["enabled"],
        "cache_ram_bytes": ram_cache,
        "cache_storage_bytes": general_cache,
        "predictable_cache_bytes": predictable_cache,
        "cache_root": str(CACHE_ROOT),
        "predictable_cache_root": str(PREDICTABLE_ROOT),
        "note": "caching and prioritization only; GPU rendering remains on the GPU",
    }

def cache_key(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

def predictable_path(game, asset):
    PREDICTABLE_ROOT.mkdir(parents=True, exist_ok=True)
    return PREDICTABLE_ROOT / cache_key(game) / cache_key(asset)

def cache_predictable(game, asset, source):
    destination = predictable_path(game, asset)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(json.dumps({"cached": True, "path": str(destination)}, indent=2))

def main():
    c = load()

    if len(sys.argv) > 1 and sys.argv[1] in ("on", "off"):
        c["enabled"] = sys.argv[1] == "on"
        CONFIG.parent.mkdir(parents=True, exist_ok=True)
        CONFIG.write_text(json.dumps(c, indent=2))

    if len(sys.argv) == 4 and sys.argv[1] == "cache":
        cache_predictable(sys.argv[2], sys.argv[3], sys.argv[3])
        return

    print(json.dumps(plan(), indent=2))

if __name__ == "__main__":
    main()
