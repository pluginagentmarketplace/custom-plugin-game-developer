#!/usr/bin/env python3
import json
def helper(): return {"techniques": ["state_sync", "prediction", "rollback"]}
if __name__ == "__main__": print(json.dumps(helper(), indent=2))
