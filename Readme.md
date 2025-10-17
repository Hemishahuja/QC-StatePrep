# QC Amplitudes — From-scratch 2- and 3-qubit state preparation

## Goal
The main idea here is to take these complex amplitudes and build a quantum state vector from scratch - Without using any fancy high-level state-prep utilities. Wit bare linear algebra stuff - normalization, shapes, and matrix-vector representations.

## Math
### Two qubits:
```
|ψ⟩ = a₀|00⟩ + a₁|01⟩ + a₂|10⟩ + a₃|11⟩, ∑|aᵢ|² = 1
```
If the input isn't normalized (which sometimes happens), we just scale it by 1/√∑|aᵢ|². Pretty straightforward!

### Three qubits:
```
|ψ⟩ = ∑aᵢ|i⟩, where i ∈ {000,...,111}
```

**Basis order:** Binary ascending (|00⟩, |01⟩, |10⟩, |11⟩) - just fyi.

## Design choices
- Strict validation (finite numbers, correct length, nonzero vector)
- Explicit complex dtype (complex128) and numerical tolerances (1e-12)
- Pretty-printer for bra-ket rendering

## Installation
```bash
pip install -e .
```

## Testing
```bash
pytest
```

## Notes
This project was created to explore quantum state preparation from first principles. It's a learning exercise to better understand the underlying linear algebra involved in quantum computing., and was created as a screening for QOSF. 
