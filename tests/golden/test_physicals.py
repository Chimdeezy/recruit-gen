import numpy as np
from recruit_gen.stages import (
    physicals
)


def test_physicals_returns_valid_recruits():
    seed = 22
    rng = np.random.default_rng(seed)
    recruits = [
        {"height" : 19}, {"height" : 0}
    ]
    recruits = physicals(recruits, rng)

    for r in recruits:
        assert r.height > 0


