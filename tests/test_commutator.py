import sympy as sp

from src.symbolic import (
    SIGMA_X,
    SIGMA_Y,
    SIGMA_Z,
    anticommutator,
    commutator,
)


def test_pauli_commutation() -> None:
    assert commutator(SIGMA_X, SIGMA_Y) == 2 * sp.I * SIGMA_Z


def test_pauli_anticommutation() -> None:
    assert anticommutator(SIGMA_X, SIGMA_Y) == sp.zeros(2)


def test_scalar_commutator_zero() -> None:
    assert commutator(sp.Integer(2), sp.Integer(3)) == 0
