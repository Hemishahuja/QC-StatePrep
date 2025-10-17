import numpy as np
import pytest
from src.stateprep import prepare_three_qubit_state, dim

def test_dimension_is_eight():
    v = prepare_three_qubit_state([1,0,0,0,0,0,0,0])
    assert dim(v) == 8

def test_normalization_from_nonunit():
    v = prepare_three_qubit_state([2,0,0,0,0,0,0,0])
    assert pytest.approx(np.vdot(v, v).real, rel=1e-12, abs=1e-12) == 1.0

def test_random_complex_normalizes():
    rng = np.random.default_rng(42)
    raw = rng.normal(size=8) + 1j*rng.normal(size=8)
    v = prepare_three_qubit_state(raw)
    assert pytest.approx(np.vdot(v, v).real, rel=1e-12, abs=1e-12) == 1.0

def test_bad_length_rejected():
    with pytest.raises(ValueError):
        prepare_three_qubit_state([1,0,0,0,0,0,0])  # 7 not allowed
