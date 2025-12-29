#!/usr/bin/env python3
import json
def analyze(): return {"areas": ["cpu", "gpu", "memory"], "techniques": ["profiling", "batching", "lod"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
