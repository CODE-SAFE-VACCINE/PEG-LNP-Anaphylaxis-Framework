#!/usr/bin/env python3
"""make_figs_5B.py — figures for Article 5B (Vaccines)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

np.random.seed(42)
OUT = Path("figures_5B"); OUT.mkdir(exist_ok=True)

# ---- simulate the virtual population ----
n = 1000
titre = np.where(np.random.random(n) < 0.30, 0.0,
                 np.where(np.random.random(n) < 0.80,
                          np.random.lognormal(0, 0.5, n),
                          np.random.lognormal(0, 0.6, n)))
H_peg = 9.44 * (1 + 0.50 * titre)
H_pgl = 1.50 * (1 + 0.02 * titre)

# ---- Fig. 1: peak histamine distributions at 0.3 mg/kg ----
fig, ax = plt.subplots(figsize=(6.5, 4.0))
bins = np.linspace(0, 40, 60)
ax.hist(H_peg, bins=bins, alpha=0.60, color="#d95f02",
        label=f"PEG-LNP  (n = {n})", density=True)
ax.hist(H_pgl, bins=bins, alpha=0.60, color="#1b9e77",
        label=f"PGL-LNP  (n = {n})", density=True)
ax.axvline(15, ls="--", lw=1.0, color="gray",
           label="Histamine threshold (15 ng/mL)")
ax.set_xlabel("Peak histamine (ng/mL) at 0.3 mg/kg")
ax.set_ylabel("Probability density")
ax.set_title("Peak histamine distributions at the standard dose")
ax.legend(frameon=False, fontsize=8.5)
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(OUT / "Fig1_histamine_distributions.pdf", bbox_inches="tight")
plt.close()
print("Wrote", OUT / "Fig1_histamine_distributions.pdf")

# ---- Fig. 2: FIH dose comparison ----
labels = ["PEG-LNP", "PGL-LNP"]
fih = [0.0043, 0.2798]
colors = ["#d95f02", "#1b9e77"]
fig, ax = plt.subplots(figsize=(5.5, 4.0))
bars = ax.bar(labels, fih, color=colors, alpha=0.85, edgecolor="black")
for b, v in zip(bars, fih):
    ax.text(b.get_x() + b.get_width()/2, v * 1.10,
            f"{v:.4f} mg/kg", ha="center", fontsize=10, fontweight="bold")
ax.set_yscale("log")
ax.set_ylim(1e-3, 1.0)
ax.set_ylabel("FIH dose (mg/kg, log scale)")
ax.set_title("FIH dose: PGL-LNP has a 64.5-fold wider safety window")
ax.grid(alpha=0.25, axis="y")
plt.tight_layout()
plt.savefig(OUT / "Fig2_FIH_comparison.pdf", bbox_inches="tight")
plt.close()
print("Wrote", OUT / "Fig2_FIH_comparison.pdf")
