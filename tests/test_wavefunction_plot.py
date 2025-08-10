import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from src.physics.infinite_square_well import wavefunction
from src.visualization import plot_wavefunction


def test_plot_wavefunction_returns_figure() -> None:
    L = 1.0
    x = np.linspace(0, L, 50)
    psi = wavefunction(1, x, L)
    fig, ax = plot_wavefunction(x, psi, probability=True)
    assert isinstance(fig, Figure)
    line = ax.lines[0]
    assert np.allclose(line.get_xdata(), x)
    assert np.allclose(line.get_ydata(), psi.real)
    prob_line = ax.lines[-1]
    assert np.allclose(prob_line.get_ydata(), np.abs(psi) ** 2)
    plt.close(fig)
