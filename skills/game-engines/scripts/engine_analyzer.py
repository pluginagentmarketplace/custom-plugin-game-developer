#!/usr/bin/env python3
import json
def analyze(): return {"engines": ["unity", "unreal", "godot"], "features": ["rendering", "physics", "scripting"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
