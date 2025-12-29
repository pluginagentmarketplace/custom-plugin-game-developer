#!/usr/bin/env python3
import json
def helper(): return {"platforms": ["unity_cloud", "github_actions"], "stages": ["build", "test", "deploy"]}
if __name__ == "__main__": print(json.dumps(helper(), indent=2))
