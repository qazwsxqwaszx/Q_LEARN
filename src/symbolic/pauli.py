"""Definitions of the Pauli matrices."""
from __future__ import annotations

import sympy as sp

__all__ = ["SIGMA_X", "SIGMA_Y", "SIGMA_Z"]

SIGMA_X = sp.Matrix([[0, 1], [1, 0]])
SIGMA_Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SIGMA_Z = sp.Matrix([[1, 0], [0, -1]])
