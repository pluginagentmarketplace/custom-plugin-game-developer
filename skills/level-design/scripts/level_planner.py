#!/usr/bin/env python3
import json
def plan(): return {"principles": ["flow", "pacing", "guidance"], "tools": ["probuilder", "terrain"]}
if __name__ == "__main__": print(json.dumps(plan(), indent=2))
