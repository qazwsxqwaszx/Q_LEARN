import numpy as np
import pytest

from src.models.harmonic_oscillator import energy_level, wavefunction
from src.physics.constants import HBAR


def test_energy_spacing() -> None:
    omega = 5.0
    e0 = energy_level(0, omega)
    e1 = energy_level(1, omega)
    assert pytest.approx(HBAR * omega, rel=1e-12) == e1 - e0


def test_ground_state_normalized() -> None:
    omega = 2.0
    mass = HBAR  # use natural units for convenience
    xs = np.linspace(-10, 10, 2000)
    dx = xs[1] - xs[0]
    psi = wavefunction(0, xs, mass=mass, omega=omega)
    integral = np.sum(np.abs(psi) ** 2 * dx)
    assert pytest.approx(1.0, rel=1e-3) == integral
