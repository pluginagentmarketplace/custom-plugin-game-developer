#!/usr/bin/env python3
import json
def manage(): return {"engines": ["fmod", "wwise"], "concepts": ["spatial", "mixing", "dynamic"]}
if __name__ == "__main__": print(json.dumps(manage(), indent=2))
