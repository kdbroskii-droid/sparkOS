#!/usr/bin/env python3
import json,shutil,subprocess,sys
NMCLI=shutil.which("nmcli")
def run(*args):
    if not NMCLI: raise RuntimeError("NetworkManager/nmcli is not installed")
    p=subprocess.run([NMCLI,*args],text=True,capture_output=True,check=False)
    if p.returncode: raise RuntimeError(p.stderr.strip() or p.stdout.strip() or "nmcli failed")
    return p.stdout.strip()
def status():
    out=run("-t","-f","ACTIVE,SSID,SIGNAL,SECURITY,DEVICE","dev","wifi"); rows=[]
    for line in out.splitlines():
        x=line.split(":")
        if len(x)>=5: rows.append({"active":x[0]=="yes","ssid":x[1],"signal":x[2],"security":x[3],"device":x[4]})
    return rows
def main():
    c=sys.argv[1:] or ["status"]
    if c[0] in ("status","scan"): print(json.dumps(status(),indent=2)); return
    if c[0]=="connect" and len(c)>=2:
        a=["dev","wifi","connect",c[1]]
        if len(c)>=3:a+=["password",c[2]]
        print(run(*a)); return
    if c[0]=="disconnect": print(run("dev","disconnect","ifname",c[1] if len(c)>1 else "")); return
    if c[0] in ("on","off"): print(run("radio","wifi",c[0])); return
    raise SystemExit("Usage: wifi.py [status|scan|connect SSID [PASSWORD]|disconnect DEVICE|on|off]")
if __name__=="__main__":
    try:main()
    except Exception as e: print("SparkOS Wi-Fi:",e,file=sys.stderr);sys.exit(1)
