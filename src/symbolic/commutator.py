"""Symbolic operator utilities."""
from __future__ import annotations

import sympy as sp

__all__ = ["commutator", "anticommutator"]


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    """Return the commutator ``[A, B] = AB - BA``."""
    return a * b - b * a


def anticommutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    """Return the anticommutator ``{A, B} = AB + BA``."""
    return a * b + b * a
