"""Plotting helpers for quantum wavefunctions."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")  # ensure headless environments work
import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence, Tuple

__all__ = ["plot_wavefunction"]


def plot_wavefunction(
    x: Sequence[float],
    psi: Sequence[complex],
    *,
    probability: bool = False,
    ax: matplotlib.axes.Axes | None = None,
) -> Tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """Plot a wavefunction and optionally its probability density.

    Parameters
    ----------
    x:
        Sequence of positions.
    psi:
        Sequence of complex wavefunction values at ``x``.
    probability:
        If ``True``, also plot the probability density ``|ψ|^2``.
    ax:
        Optional Matplotlib axes to draw on.

    Returns
    -------
    Tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]
        The figure and axes containing the plot.
    """
    x_arr = np.asarray(x, dtype=float)
    psi_arr = np.asarray(psi, dtype=complex)
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure
    ax.plot(x_arr, psi_arr.real, label="Re(ψ)")
    if np.any(np.abs(psi_arr.imag) > 1e-12):
        ax.plot(x_arr, psi_arr.imag, label="Im(ψ)")
    if probability:
        ax.plot(x_arr, np.abs(psi_arr) ** 2, label="|ψ|²")
    ax.set_xlabel("x")
    ax.set_ylabel("ψ")
    ax.legend()
    return fig, ax
