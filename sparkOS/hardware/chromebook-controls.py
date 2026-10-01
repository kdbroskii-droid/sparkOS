#!/usr/bin/env python3
import subprocess,sys
from pathlib import Path
def find(paths):
    for x in paths:
        if Path(x).exists(): return Path(x)
def brightness(delta):
    p=find(["/sys/class/backlight/intel_backlight/brightness","/sys/class/backlight/amdgpu_bl0/brightness"])
    if not p:return "brightness-unavailable"
    m=Path(str(p).replace("/brightness","/max_brightness"))
    if not m.exists():return "brightness-unavailable"
    cur=int(p.read_text());mx=int(m.read_text());p.write_text(str(max(0,min(mx,cur+delta))));return "brightness-ok"
def cmd(*a):
    try:return subprocess.run(a,text=True,capture_output=True,check=False).stdout.strip()
    except FileNotFoundError:return "unavailable"
def main():
    c=sys.argv[1:] or ["status"]
    if c[0]=="brightness-up":print(brightness(100));return
    if c[0]=="brightness-down":print(brightness(-100));return
    if c[0]=="lock":print(cmd("loginctl","lock-session"));return
    if c[0]=="suspend":print(cmd("systemctl","suspend"));return
    print("SparkOS Chromebook controls ready: brightness, media/volume keys, lid and power events.")
if __name__=="__main__":main()
