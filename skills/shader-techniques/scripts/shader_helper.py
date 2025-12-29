#!/usr/bin/env python3
import json
def helper(): return {"languages": ["hlsl", "glsl"], "types": ["vertex", "fragment", "compute"]}
if __name__ == "__main__": print(json.dumps(helper(), indent=2))
