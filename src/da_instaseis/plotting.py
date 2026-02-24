"""
Plotting utilities for da-instaseis.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_waveforms(st, title=None, figsize=(10, 6)):
    """
    Plot an ObsPy stream of seismograms.

    Parameters
    ----------
    st : obspy.Stream
        Stream of seismic traces to plot.
    title : str, optional
        Figure title.
    figsize : tuple, optional
        Figure size in inches.

    Returns
    -------
    fig : matplotlib.figure.Figure
    axes : list of matplotlib.axes.Axes
    """
    n = len(st)
    fig, axes = plt.subplots(n, 1, figsize=figsize, sharex=True)
    if n == 1:
        axes = [axes]

    for ax, tr in zip(axes, st):
        times = tr.times()
        ax.plot(times, tr.data, "k", lw=0.8)
        ax.set_ylabel(tr.stats.channel)
        ax.set_xlim(times[0], times[-1])

    axes[-1].set_xlabel("Time (s)")
    if title:
        fig.suptitle(title)
    fig.tight_layout()
    return fig, axes


def plot_misfit_history(misfit_history, figsize=(7, 4)):
    """
    Plot the misfit reduction over iterations.

    Parameters
    ----------
    misfit_history : array_like
        Sequence of misfit values per iteration.
    figsize : tuple, optional
        Figure size in inches.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(np.arange(len(misfit_history)), misfit_history, "o-")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Misfit")
    ax.set_title("Misfit history")
    fig.tight_layout()
    return fig, ax
