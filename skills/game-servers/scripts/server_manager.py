#!/usr/bin/env python3
import json
def manage(): return {"types": ["authoritative", "relay"], "services": ["photon", "playfab"]}
if __name__ == "__main__": print(json.dumps(manage(), indent=2))
