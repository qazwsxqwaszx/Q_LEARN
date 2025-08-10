"""Analytical solutions for the 1D quantum harmonic oscillator."""
from __future__ import annotations

import math

import numpy as np
from scipy.special import eval_hermite

from src.physics.constants import HBAR, M_ELECTRON

__all__ = ["wavefunction", "energy_level"]


def wavefunction(
    n: int,
    x: float | np.ndarray,
    mass: float = M_ELECTRON,
    omega: float = 1.0,
) -> np.ndarray:
    """Return the stationary state wavefunction ``ψ_n(x)``.

    Parameters
    ----------
    n:
        Quantum number (n ≥ 0).
    x:
        Position or array of positions.
    mass:
        Particle mass in kilograms. Defaults to the electron mass.
    omega:
        Oscillation angular frequency in rad/s. Defaults to 1.

    Returns
    -------
    numpy.ndarray
        Value of ``ψ_n(x)``.
    """
    if n < 0:
        raise ValueError("Quantum number n must be >= 0")
    x_arr = np.asarray(x, dtype=float)
    alpha = math.sqrt(mass * omega / HBAR)
    xi = alpha * x_arr
    prefactor = (mass * omega / (math.pi * HBAR)) ** 0.25
    normalization = prefactor / math.sqrt(2**n * math.factorial(n))
    return normalization * eval_hermite(n, xi) * np.exp(-xi**2 / 2)


def energy_level(n: int, omega: float = 1.0) -> float:
    """Return the energy ``E_n`` of the ``n`` th level in Joules."""
    if n < 0:
        raise ValueError("Quantum number n must be >= 0")
    return HBAR * omega * (n + 0.5)
