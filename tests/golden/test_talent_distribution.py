import numpy as np
from recruit_gen.pipeline import (
    run_pipeline
)
from recruit_gen.cli import (
    write_csv
)
import typer
import csv
import json
from recruit_gen.pipeline import run_pipeline


def test_talent_pyramid_shape():
    rng = np.random.default_rng(42)

    # draw 1000 talents using your stage's logic
    recruits = run_pipeline(count=1000, seed = 42)

    # print(recruits[0])
    talent_scores = [r['talent'] for r in recruits]

    median = np.percentile(talent_scores, 50)
    p99 = np.percentile(talent_scores, 99)


    # print(f"median={median:.2f}  p99={p99:.2f}  ratio={p99/median:.2f}")

    # assert p99 / median > 0.25  
    assert p99 / median > 4.0


def test_golden_seed42():
    fresh = run_pipeline(count=80, seed=42)

    with open("tests/golden/basketball_seed42.json") as f:
        golden = json.load(f)

    assert fresh == golden