#!/usr/bin/env python3
import json
def analyze(): return {"models": ["premium", "f2p", "subscription"], "features": ["iap", "battle_pass"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
