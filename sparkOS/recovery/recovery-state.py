#!/usr/bin/env python3
import sys
states={"green":"GREEN: recovery ready","red":"RED: recovery integrity failure","reset":"BLACK: factory reset in progress"}
state=sys.argv[1].lower() if len(sys.argv)>1 else "green"
if state not in states:raise SystemExit("Use green, red or reset")
print(states[state])
