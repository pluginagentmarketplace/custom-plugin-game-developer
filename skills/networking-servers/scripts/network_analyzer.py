#!/usr/bin/env python3
import json
def analyze(): return {"models": ["client_server", "p2p"], "protocols": ["tcp", "udp"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
