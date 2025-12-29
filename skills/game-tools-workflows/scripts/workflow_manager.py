#!/usr/bin/env python3
import json
def manage(): return {"vcs": ["git", "perforce"], "pm": ["jira", "hacknplan"]}
if __name__ == "__main__": print(json.dumps(manage(), indent=2))
