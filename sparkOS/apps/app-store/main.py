#!/usr/bin/env python3
"""SparkOS App Store service prototype.
The GUI is separate; this process owns package discovery/install requests."""
import json
from pathlib import Path

STATE=Path.home()/".local/share/sparkos/installed.json"

def installed():
    try:return json.loads(STATE.read_text())
    except Exception:return []

def register(package):
    items=installed()
    if package not in items: items.append(package)
    STATE.parent.mkdir(parents=True,exist_ok=True);STATE.write_text(json.dumps(items,indent=2))

def main():
    print("SparkOS App Store service")
    print("Commands: installed, register <package>, quit")
    while True:
        try:cmd=input("Store$ ").strip()
        except EOFError:break
        if cmd in ("quit","exit"):break
        if cmd=="installed": print("\\n".join(installed()) or "No apps installed")
        elif cmd.startswith("register "): register(cmd[9:].strip());print("Registered")
        else: print("Unknown Store command")

if __name__=="__main__":main()
