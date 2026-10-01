#!/usr/bin/env python3
"""SparkOS Files application prototype.
Native implementation target: compiled SparkOS file-manager binary."""
from pathlib import Path
import os

HOME=Path.home()
ROOTS=[("Home",HOME),("Downloads",HOME/"Downloads"),("Documents",HOME/"Documents"),("Pictures",HOME/"Pictures")]

def list_dir(path):
    try:return sorted(path.iterdir(),key=lambda p:(not p.is_dir(),p.name.lower()))
    except PermissionError:return []

def main():
    print("SparkOS Files")
    print("Commands: ls [path], cd <path>, open <path>, pwd, quit")
    cwd=HOME
    while True:
        try: cmd=input(f"Files:{cwd}$ ").strip()
        except EOFError: break
        if cmd in ("quit","exit"): break
        if cmd=="pwd": print(cwd); continue
        if cmd.startswith("cd "):
            p=Path(cmd[3:].strip()).expanduser(); p=(cwd/p if not p.is_absolute() else p).resolve()
            if p.is_dir(): cwd=p
            else: print("Not a directory")
        elif cmd.startswith("ls"):
            raw=cmd[2:].strip(); p=(cwd/ raw if raw and not Path(raw).is_absolute() else Path(raw or cwd)).expanduser()
            for x in list_dir(p): print(("[DIR] " if x.is_dir() else "      ")+x.name)
        elif cmd.startswith("open "):
            p=(cwd/Path(cmd[5:].strip()).expanduser()).resolve(); print("Selected:",p)
        else: print("Unknown Files command")

if __name__=="__main__": main()
