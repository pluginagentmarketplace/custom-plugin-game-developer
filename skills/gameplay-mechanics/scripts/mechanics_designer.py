#!/usr/bin/env python3
import json
def design(): return {"types": ["movement", "combat", "inventory"], "patterns": ["state_machine", "event_driven"]}
if __name__ == "__main__": print(json.dumps(design(), indent=2))
