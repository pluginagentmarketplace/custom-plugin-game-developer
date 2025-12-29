#!/usr/bin/env python3
import json
def analyze(): return {"patterns": ["ecs", "component", "state_machine"], "principles": ["solid", "dry"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
