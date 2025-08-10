"""Utilities for the one-dimensional infinite square well problem.

Provides analytical solutions for the particle-in-a-box model. These
functions are intentionally lightweight so they can be used in both the
GUI application and unit tests without requiring heavy dependencies.
"""
from __future__ import annotations

import math

import numpy as np

from .constants import HBAR, M_ELECTRON

__all__ = ["wavefunction", "energy_level"]


def wavefunction(n: int, x: float | np.ndarray, length: float) -> np.ndarray:
    """Return the stationary state wavefunction ``ψ_n(x)``.

    Parameters
    ----------
    n:
        Quantum number (n ≥ 1).
    x:
        Position or array of positions within the well ``0 ≤ x ≤ L``.
    length:
        Width ``L`` of the potential well in metres.

    Returns
    -------
    numpy.ndarray
        The value of the wavefunction at ``x``.
    """
    if n < 1:
        raise ValueError("Quantum number n must be >= 1")
    prefactor = math.sqrt(2.0 / length)
    # Use numpy to allow vectorised evaluation
    x_arr = np.asarray(x, dtype=float)
    return prefactor * np.sin(n * math.pi * x_arr / length)


def energy_level(n: int, length: float, mass: float = M_ELECTRON) -> float:
    """Return the energy ``E_n`` of the ``n`` th level in Joules.

    Parameters
    ----------
    n:
        Quantum number (n ≥ 1).
    length:
        Width ``L`` of the potential well in metres.
    mass:
        Mass of the particle in kilograms. Defaults to electron mass.

    Returns
    -------
    float
        The energy in Joules.
    """
    if n < 1:
        raise ValueError("Quantum number n must be >= 1")
    return (n ** 2 * math.pi ** 2 * HBAR ** 2) / (2.0 * mass * length ** 2)
