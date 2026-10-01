#!/usr/bin/env python3
import json,shutil,sys
from pathlib import Path
CONFIG=Path("/etc/sparkos/gaming.json")
DEFAULT={"enabled":False,"max_free_ram_fraction":0.35,"max_free_storage_fraction":0.35,"ram_reserve_mb":512,"storage_reserve_gb":8}
def load():
    try:return {**DEFAULT,**json.loads(CONFIG.read_text())}
    except Exception:return DEFAULT.copy()
def stats():
    ram=0
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):ram=int(line.split()[1])*1024;break
    d=shutil.disk_usage("/")
    return {"free_ram_bytes":ram,"free_storage_bytes":d.free}
def plan():
    c=load();s=stats()
    ram=max(0,min(int(s["free_ram_bytes"]*c["max_free_ram_fraction"]),s["free_ram_bytes"]-c["ram_reserve_mb"]*1024**2))
    storage=max(0,min(int(s["free_storage_bytes"]*c["max_free_storage_fraction"]),s["free_storage_bytes"]-c["storage_reserve_gb"]*1024**3))
    return {"enabled":c["enabled"],"cache_ram_bytes":ram,"cache_storage_bytes":storage,"note":"cache and prioritization only"}
def main():
    c=load()
    if len(sys.argv)>1 and sys.argv[1] in ("on","off"):
        c["enabled"]=sys.argv[1]=="on";CONFIG.parent.mkdir(parents=True,exist_ok=True);CONFIG.write_text(json.dumps(c,indent=2))
    print(json.dumps(plan(),indent=2))
if __name__=="__main__":main()
