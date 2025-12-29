#!/usr/bin/env python3
import json
def helper(): return {"daws": ["ableton", "fl_studio", "reaper"], "concepts": ["midi", "mixing", "adaptive"]}
if __name__ == "__main__": print(json.dumps(helper(), indent=2))
