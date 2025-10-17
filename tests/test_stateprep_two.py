import numpy as np
import pytest
from src.stateprep import prepare_two_qubit_state, dim, BASIS_2Q

def test_dimension_is_four():
    v = prepare_two_qubit_state([1,0,0,0])
    assert dim(v) == 4
    assert v.dtype == np.complex128

def test_normalization_enforced_from_nonunit():
    v = prepare_two_qubit_state([2,0,0,0])  # norm 2 -> should normalize
    assert pytest.approx(np.vdot(v, v).real, rel=1e-12, abs=1e-12) == 1.0
    assert np.allclose(v, np.array([1+0j,0,0,0], dtype=np.complex128))

def test_random_complex_normalizes():
    rng = np.random.default_rng(7)
    raw = rng.normal(size=4) + 1j*rng.normal(size=4)
    v = prepare_two_qubit_state(raw)
    assert pytest.approx(np.vdot(v, v).real, rel=1e-12, abs=1e-12) == 1.0

def test_zero_vector_rejected():
    with pytest.raises(ValueError):
        prepare_two_qubit_state([0,0,0,0])

def test_finite_numbers_required():
    with pytest.raises(ValueError):
        prepare_two_qubit_state([1, 0, np.inf, 0])

def test_basis_order_documented():
    v = prepare_two_qubit_state([1,0,0,0])
    # |00⟩ should be first basis element by spec
    assert np.allclose(v, np.array([1,0,0,0], dtype=np.complex128))
