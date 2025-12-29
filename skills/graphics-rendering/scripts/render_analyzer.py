#!/usr/bin/env python3
import json
def analyze(): return {"pipelines": ["forward", "deferred"], "techniques": ["pbr", "ssao", "bloom"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
