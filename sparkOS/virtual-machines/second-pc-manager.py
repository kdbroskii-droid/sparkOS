#!/usr/bin/env python3
"""SparkOS Second PC manager."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("/var/lib/sparkos/second-pc")
CONFIG = ROOT / "config.json"
DEFAULT = {"name":"SparkOS Second PC","ram_mb":2048,"cpus":2,"disk_gb":32,"network":"sparklink","shared_clipboard":False,"shared_files":False}

def load():
    ROOT.mkdir(parents=True, exist_ok=True)
    if CONFIG.exists():
        try: return {**DEFAULT, **json.loads(CONFIG.read_text())}
        except Exception: pass
    CONFIG.write_text(json.dumps(DEFAULT, indent=2))
    return DEFAULT.copy()

def ensure_disk(c):
    disk = ROOT / "second-pc.qcow2"
    if not disk.exists():
        subprocess.run(["qemu-img","create","-f","qcow2",str(disk),f"{c["disk_gb"]}G"], check=True)
    return disk

def qemu_command(c):
    disk = ROOT / "second-pc.qcow2"
    return ["qemu-system-x86_64","-enable-kvm","-m",str(c["ram_mb"]),"-smp",str(c["cpus"]),"-drive",f"file={disk},format=qcow2,if=virtio","-netdev","user,id=sparklink","-device","virtio-net-pci,netdev=sparklink"]

def main():
    c = load()
    action = sys.argv[1] if len(sys.argv) > 1 else "status"
    if action == "create":
        print(f"Second PC disk ready: {ensure_disk(c)}")
    elif action == "command":
        ensure_disk(c); print(" ".join(qemu_command(c)))
    elif action == "status":
        print(json.dumps({"name":c["name"],"network":c["network"],"disk":str(ROOT/"second-pc.qcow2"),"isolated_by_default":True}, indent=2))
    else: raise SystemExit("Usage: second-pc-manager.py [create|command|status]")

if __name__ == "__main__": main()