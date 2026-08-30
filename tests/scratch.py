import json
from recruit_gen.pipeline import run_pipeline

recruits = run_pipeline(count=80, seed=42)
with open("tests/golden/basketball_seed42.json", "w") as f:
    json.dump(recruits, f, indent=2)