import numpy as np
# Lets convert the complex amplitudes vector into some pretty Dirac Notation 
# [0.7071+0j, 0.0+0j, 0.0+0j, 0.7071j]  →  0.707100|00⟩ + (0.000000+0.707100i)|11⟩

def bra_ket(vec: np.ndarray, basis_labels) -> str:
    """
    Render c0|b0⟩ + c1|b1⟩ + ... with compact complex formatting.
        
    """
    terms = []
    tol = 1e-12
    for c, lbl in zip(vec, basis_labels):
        if abs(c) > tol:
            re = f"{c.real:.6f}"
            im = f"{c.imag:+.6f}i"
            if abs(c.imag) < tol:
                terms.append(f"{re}{'' if re.startswith('-') else ''}{''}|{lbl[1:]}")
                terms[-1] = f"{float(re):.6f}{lbl}"
            else:
                terms.append(f"({re}{im}){lbl}")
    return " + ".join(terms) if terms else "0"
