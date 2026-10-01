#!/usr/bin/env python3
"""SparkOS Settings application with wireless controls."""
import json,shutil,subprocess,sys
from pathlib import Path
CONFIG=Path.home()/".config"/"sparkos"/"settings.json"
DEFAULT={"theme":"dark","animations":True,"gaming_mode":False,"keyboard_layout":"chromebook"}
def load():
    try:return {**DEFAULT,**json.loads(CONFIG.read_text())}
    except Exception:return DEFAULT.copy()
def save(data):
    CONFIG.parent.mkdir(parents=True,exist_ok=True);CONFIG.write_text(json.dumps(data,indent=2))
def tool(script,*args):
    path=Path(__file__).resolve().parents[2]/"system"/"network"/script
    p=subprocess.run([sys.executable,str(path),*args],text=True,capture_output=True,check=False)
    print(p.stdout.strip() or p.stderr.strip())
def main():
    data=load();print("SparkOS Settings");print(json.dumps(data,indent=2))
    print("Commands: get <name>, set <name> <value>, wifi <args>, bluetooth <args>, quit")
    while True:
        try:cmd=input("Settings$ ").strip()
        except EOFError:break
        parts=cmd.split()
        if cmd in ("quit","exit"):break
        if len(parts)>=2 and parts[0]=="get":print(data.get(parts[1],"Unknown setting"));continue
        if len(parts)==3 and parts[0]=="set":
            value=parts[2]
            if value.lower() in ("true","false"):value=value.lower()=="true"
            data[parts[1]]=value;save(data);print("Saved");continue
        if parts and parts[0]=="wifi":tool("wifi.py",*parts[1:]);continue
        if parts and parts[0]=="bluetooth":tool("bluetooth.py",*parts[1:]);continue
        print("Unknown Settings command")
if __name__=="__main__":main()
