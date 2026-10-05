#!/usr/bin/env python3
import json
import subprocess
import time
from pathlib import Path

CONFIG = Path("/etc/sparkos/gaming.json")
BOOST = "/usr/local/bin/sparkboost"

DEFAULT_GAMES = [
    "FortniteClient-Win64-Shipping.exe",
    "FortniteClient-Win64-Shipping",
]

def load():
    try:
        return json.loads(CONFIG.read_text())
    except Exception:
        return {"enabled": False, "auto_games": DEFAULT_GAMES}

def processes():
    result = set()
    for p in Path("/proc").iterdir():
        if not p.name.isdigit():
            continue
        try:
            cmd = (p / "cmdline").read_bytes().replace(b"\0", b" ").decode(errors="ignore")
            if cmd:
                result.add(cmd)
        except Exception:
            pass
    return result

def game_running(names):
    text = "\n".join(processes()).lower()
    return any(name.lower() in text for name in names)

last = None
while True:
    c = load()
    if c.get("game_mode", "auto") != "auto":
        time.sleep(5)
        continue
    running = game_running(c.get("auto_games", DEFAULT_GAMES))
    if running != last:
        subprocess.run([BOOST, "on" if running else "off"], check=False)
        last = running
    time.sleep(5)
