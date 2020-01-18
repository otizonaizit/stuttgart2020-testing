import numpy as np
import pytest

# set the random seed for once here
SEED = np.random.randint(0,2**31)


@pytest.fixture(autouse=True)
def set_seed():
    print(f'Using seed {SEED}')
    np.random.seed(SEED)

