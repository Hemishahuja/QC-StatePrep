import numpy as np
from .linalg_utils import as_complex_array, normalize

BASIS_2Q = ("|00⟩", "|01⟩", "|10⟩", "|11⟩")
BASIS_3Q = tuple(f"|{b:03b}⟩" for b in range(8))

def prepare_two_qubit_state(amplitudes) -> np.ndarray:
    """
    Return a normalized 4-vector |ψ⟩ = a0|00⟩ + a1|01⟩ + a2|10⟩ + a3|11⟩.
    - Input can be non-normalized; we normalize internally.
    """
    vec = as_complex_array(amplitudes, expected_len=4)
    return normalize(vec)

def prepare_three_qubit_state(amplitudes) -> np.ndarray:
    """
    Stretch goal: normalized 8-vector |ψ⟩ = Σ_{i=0}^{7} a_i |i⟩ (binary order 000..111).
    """
    vec = as_complex_array(amplitudes, expected_len=8)
    return normalize(vec)

def dim(vec: np.ndarray) -> int:
    return vec.size
