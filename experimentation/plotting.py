import numpy as np
from matplotlib import pyplot as plt


def plot_pvalues(pvalues):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax2.plot(sorted(pvalues), np.linspace(0, 1, len(pvalues)), linewidth=2)
    ax2.plot([0, 1], [0, 1], "--k")
    ax2.set_xlim(-0.01, 1.01)
    ax2.set_ylim(-0.01, 1.01)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xlabel("p-value")
    ax2.set_ylabel("CDF")

    ax1.hist(pvalues, density=True)
    ax1.plot([0, 1], [1, 1], "--k")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_xlabel("p-value")
    return fig, (ax1, ax2)
