"""Core quantum state utilities."""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass
class QuantumState:
    """Represent a normalized quantum state vector.

    The vector is automatically normalized upon instantiation. The class
    provides convenience methods for computing measurement probabilities
    and expectation values of Hermitian operators.
    """

    vector: np.ndarray

    def __post_init__(self) -> None:
        vec = np.asarray(self.vector, dtype=complex)
        norm = np.linalg.norm(vec)
        if norm == 0:
            raise ValueError("State vector cannot be the zero vector")
        self.vector = vec / norm

    def probability(self, index: int) -> float:
        """Return the probability of measuring the basis state ``index``."""
        if index < 0 or index >= self.vector.size:
            raise IndexError("Index out of bounds")
        amp = self.vector[index]
        return float(np.abs(amp) ** 2)

    def expectation(self, operator: np.ndarray) -> complex:
        """Return the expectation value of an operator for this state."""
        op = np.asarray(operator, dtype=complex)
        if op.shape != (self.vector.size, self.vector.size):
            raise ValueError("Operator shape must match state dimension")
        return complex(np.vdot(self.vector, op @ self.vector))
