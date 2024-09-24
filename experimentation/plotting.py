import numpy as np
import scipy as sp
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


def plot_distributions(control, treatment):
    fig, ax = plt.subplots()
    mean_control = control.mean()
    std_mean_control = control.mean() / np.sqrt(len(control))
    mean_treatment = treatment.mean()
    std_mean_treatment = treatment.mean() / np.sqrt(len(treatment))
    std_control = std_mean_control
    std_treatment = std_mean_treatment
    norm = sp.stats.norm
    # Generate points on the x-axis
    x = np.linspace(
        mean_control - 4 * std_control, mean_treatment + 4 * std_treatment, 1000
    )
    # Calculate the Gaussian distributions
    control_dist = norm.pdf(x, mean_control, std_control)
    treatment_dist = norm.pdf(x, mean_treatment, std_treatment)
    # Plot the Gaussian distributions
    (control_line,) = plt.plot(x, control_dist, label="Control", linewidth=2)
    (treatment_line,) = plt.plot(x, treatment_dist, label="Treatment", linewidth=2)
    # Shade the area under the Gaussian distributions
    plt.fill_between(x, control_dist, alpha=0.2, color=control_line.get_color())
    plt.fill_between(x, treatment_dist, alpha=0.2, color=treatment_line.get_color())
    # Add direct labeling
    plt.text(
        mean_control,
        max(control_dist) * 0.7,
        "Control",
        fontsize=12,
        ha="center",
        color=control_line.get_color(),
    )
    plt.text(
        mean_treatment,
        max(treatment_dist) * 0.6,
        "Treatment",
        fontsize=12,
        ha="center",
        color=treatment_line.get_color(),
    )
    # Calculate the z-score and p-value
    z_score = (mean_treatment - mean_control) / np.sqrt(
        std_control**2 + std_treatment**2
    )
    p_value = 1 - norm.cdf(abs(z_score))
    effect = mean_treatment - mean_control
    std_effect = np.sqrt(std_control**2 + std_treatment**2)
    # Customize the plot
    ax.set_xlabel("Mean")
    ax.set_ylabel("Probability Density")
    ax.set_title(rf"effect = {effect:.2f}$\pm${std_effect:.2f}\np-value={p_value:.2f}")
    fig.tight_layout()
    return fig, ax
