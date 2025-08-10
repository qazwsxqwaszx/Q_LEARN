import numpy as np
import pytest

from src.physics.infinite_square_well import energy_level, wavefunction


def test_wavefunction_boundaries():
    L = 1.0
    x = np.array([0.0, L])
    psi = wavefunction(1, x, L)
    assert np.allclose(psi, 0.0)


def test_wavefunction_normalization():
    L = 1.0
    xs = np.linspace(0, L, 1000)
    dx = xs[1] - xs[0]
    psi = wavefunction(3, xs, L)
    prob_density = np.abs(psi) ** 2
    integral = prob_density.sum() * dx
    assert pytest.approx(1.0, rel=1e-3) == integral


def test_energy_level_increases_with_n():
    L = 1e-9
    e1 = energy_level(1, L)
    e2 = energy_level(2, L)
    assert e2 > e1
    # Energy scales as n^2
    assert pytest.approx(e1 * 4, rel=1e-12) == e2
