#!/usr/bin/env python3
"""SparkOS Settings application prototype."""
import json
from pathlib import Path
CONFIG=Path.home()/".config"/"sparkos"/"settings.json"
DEFAULT={"theme":"dark","animations":True,"gaming_mode":False,"keyboard_layout":"chromebook"}

def load():
    try:return {**DEFAULT,**json.loads(CONFIG.read_text())}
    except Exception:return DEFAULT.copy()

def save(data):
    CONFIG.parent.mkdir(parents=True,exist_ok=True);CONFIG.write_text(json.dumps(data,indent=2))

def main():
    data=load();print("SparkOS Settings");print(json.dumps(data,indent=2))
    print("Commands: get <name>, set <name> <value>, quit")
    while True:
        try: cmd=input("Settings$ ").strip()
        except EOFError: break
        if cmd in ("quit","exit"): break
        parts=cmd.split(maxsplit=2)
        if len(parts)>=2 and parts[0]=="get": print(data.get(parts[1],"Unknown setting"))
        elif len(parts)==3 and parts[0]=="set":
            value=parts[2]
            if value.lower() in ("true","false"): value=value.lower()=="true"
            data[parts[1]]=value;save(data);print("Saved")
        else: print("Unknown Settings command")

if __name__=="__main__": main()
