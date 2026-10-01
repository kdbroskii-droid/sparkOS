#!/usr/bin/env python3
import shutil,subprocess,sys
CTL=shutil.which("bluetoothctl")
def run(*args):
    if not CTL: raise RuntimeError("BlueZ bluetoothctl is not installed")
    p=subprocess.run([CTL,*args],text=True,capture_output=True,check=False)
    if p.returncode: raise RuntimeError(p.stderr.strip() or p.stdout.strip() or "bluetoothctl failed")
    return p.stdout.strip()
def main():
    c=sys.argv[1:] or ["show"]
    if c[0] in ("show","devices"):print(run(*c));return
    if c[0] in ("scan","stop-scan"):print(run("scan","on" if c[0]=="scan" else "off"));return
    if c[0] in ("on","off"):print(run("power",c[0]));return
    if c[0] in ("pair","connect","trust","remove") and len(c)>=2:print(run(c[0],c[1]));return
    raise SystemExit("Usage: bluetooth.py [show|devices|scan|stop-scan|on|off|pair MAC|connect MAC|trust MAC|remove MAC]")
if __name__=="__main__":
    try:main()
    except Exception as e:print("SparkOS Bluetooth:",e,file=sys.stderr);sys.exit(1)
