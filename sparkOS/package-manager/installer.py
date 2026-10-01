#!/usr/bin/env python3
"""SparkOS package-service prototype for EXK, APK and EXE files."""
import shutil,subprocess,sys
from pathlib import Path

def runtime_for(path):
    ext=Path(path).suffix.lower()
    if ext==".apk": return "android"
    if ext==".exe": return "windows"
    if ext==".exk": return "sparkos"
    raise ValueError("Unsupported package type")

def install(path):
    path=Path(path).resolve()
    if not path.is_file(): raise FileNotFoundError(path)
    runtime=runtime_for(path)
    if runtime=="sparkos":
        print("Registering EXK package:",path)
        return 0
    if runtime=="android":
        adb=shutil.which("adb")
        if not adb: raise RuntimeError("Android runtime is not installed")
        return subprocess.call([adb,"install",str(path)])
    wine=shutil.which("wine")
    if not wine: raise RuntimeError("Windows compatibility runtime is not installed")
    return subprocess.call([wine,str(path)])

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: spark-install <file.exk|file.apk|file.exe>",file=sys.stderr);sys.exit(2)
    try: sys.exit(install(sys.argv[1]))
    except Exception as e: print("SparkOS installer:",e,file=sys.stderr);sys.exit(1)
