#!/usr/bin/env python3
import json
def select(): return {"game": ["csharp", "cpp"], "scripting": ["lua", "gdscript"]}
if __name__ == "__main__": print(json.dumps(select(), indent=2))
