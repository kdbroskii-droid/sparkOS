#!/usr/bin/env python3
"""SparkOS Terminal application prototype."""
import os,subprocess

def main():
    print("SparkOS Terminal")
    while True:
        try: command=input("sparkOS@desktop:~$ ")
        except EOFError: break
        if command.strip() in ("exit","quit"): break
        if not command.strip(): continue
        try: subprocess.run(command,shell=True,check=False)
        except Exception as e: print("Terminal error:",e)

if __name__=="__main__": main()
