import numpy as np
# In this task we use numpy ndarrays with complex12 (i.e. real + img parts) dtype, instead of regular Python lists. They computer faster and are easirer to manage. 
def as_complex_array(a, expected_len: int) -> np.ndarray:
    arr = np.asarray(a, dtype=np.complex128).flatten()
    if arr.size != expected_len:
        raise ValueError(f"Expected {expected_len} amplitudes, got {arr.size}.")
    if not np.all(np.isfinite(arr)):
        raise ValueError("Amplitudes must be finite numbers.")
    if np.allclose(arr, 0):
        raise ValueError("Amplitude vector cannot be the zero vector.")
    return arr

def normalize(vec: np.ndarray, eps: float = 1e-15) -> np.ndarray:
    norm2 = float(np.vdot(vec, vec).real)  # ||ψ||^2
    if norm2 <= eps:
        raise ValueError("Vector norm too small to normalize.")
    return vec / np.sqrt(norm2)

def kron(*matrices: np.ndarray) -> np.ndarray:
    """Left-associative Kronecker product: kron(A, B, C) = A ⊗ B ⊗ C."""
    out = matrices[0]
    for m in matrices[1:]:
        out = np.kron(out, m)
    return out
