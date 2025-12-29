#!/usr/bin/env python3
import json
def helper(): return {"platforms": ["steam", "epic", "mobile"], "requirements": ["cert", "ratings"]}
if __name__ == "__main__": print(json.dumps(helper(), indent=2))
