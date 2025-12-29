#!/usr/bin/env python3
import json
def design(): return {"systems": ["niagara", "vfx_graph"], "effects": ["fire", "smoke", "magic"]}
if __name__ == "__main__": print(json.dumps(design(), indent=2))
