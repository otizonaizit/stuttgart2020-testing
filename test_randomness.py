import numpy as np

def test_random():
    x = np.random.random()
    assert x > 0


def test_random2():
    x = np.random.random()
    assert x < 0.00001

