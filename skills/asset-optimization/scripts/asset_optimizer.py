#!/usr/bin/env python3
import json
def optimize(): return {"types": ["textures", "meshes", "audio"], "techniques": ["compression", "streaming"]}
if __name__ == "__main__": print(json.dumps(optimize(), indent=2))
