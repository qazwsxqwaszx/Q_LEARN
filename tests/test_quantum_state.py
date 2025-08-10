import numpy as np
import pytest

from src.core import QuantumState


def test_normalization() -> None:
    qs = QuantumState([1, 1])
    assert np.isclose(np.linalg.norm(qs.vector), 1.0)


def test_probability() -> None:
    qs = QuantumState([1, 1])
    assert pytest.approx(qs.probability(0)) == 0.5


def test_expectation_value() -> None:
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    qs_up = QuantumState([1, 0])
    qs_down = QuantumState([0, 1])
    assert pytest.approx(qs_up.expectation(sigma_z)) == 1.0
    assert pytest.approx(qs_down.expectation(sigma_z)) == -1.0


def test_zero_vector_raises() -> None:
    with pytest.raises(ValueError):
        QuantumState([0, 0])
