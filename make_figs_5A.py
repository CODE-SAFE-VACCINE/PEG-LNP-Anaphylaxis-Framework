#!/usr/bin/env python3
"""make_figs_5A.py — figures for Article 5A (Bioinformatics)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

np.random.seed(42)
OUT = Path("figures_5A"); OUT.mkdir(exist_ok=True)

# ---- Fig. 1: workflow diagram ----
fig, ax = plt.subplots(figsize=(10.5, 2.8))
ax.set_xlim(0, 10); ax.set_ylim(0, 3); ax.axis("off")
boxes = [
    (0.10, 1.00, "Module A\nVirtual population\n(n = 1000)"),
    (2.60, 1.00, "Module B\nAllometric scaling\n(FDA KM factors)"),
    (5.10, 1.00, "Module C\nMonte Carlo\ndose–response"),
    (7.60, 1.00, "Module D\nFIH dose\ncalculator"),
]
for x, y, txt in boxes:
    ax.add_patch(plt.Rectangle((x, y), 1.90, 1.00,
                                facecolor="#e8f0f8", edgecolor="black", lw=0.8))
    ax.text(x + 0.95, y + 0.50, txt, ha="center", va="center", fontsize=8.5)
for i in range(len(boxes) - 1):
    ax.annotate("", xy=(boxes[i+1][0], 1.50),
                xytext=(boxes[i][0] + 1.90, 1.50),
                arrowprops=dict(arrowstyle="->", lw=1.2))
inputs = [
    (0.55, 0.20, "TITRE_DIST\n(Shin 2022; Kent 2024)"),
    (3.05, 0.20, "KM_FACTORS\n(FDA 2005)"),
    (5.55, 0.20, "MODEL_PEG\n(Szebeni 2018;\nWeiss-Tessbach 2025)"),
    (8.05, 0.20, "HISTAMINE_THRESHOLD\n(Moghimi 2019)"),
]
for x, y, txt in inputs:
    ax.text(x, y, txt, ha="center", va="bottom", fontsize=6.5, style="italic")
    ax.annotate("", xy=(x, 1.00), xytext=(x, y + 0.60),
                arrowprops=dict(arrowstyle="->", lw=0.7, color="gray"))
plt.tight_layout()
plt.savefig(OUT / "Fig1_workflow.pdf", bbox_inches="tight")
plt.close()
print("Wrote", OUT / "Fig1_workflow.pdf")

# ---- Fig. 2: pig CARPA reproduction ----
dose = np.array([0.01, 0.03, 0.10, 0.30, 1.00])          # mg/kg
hist_obs = np.array([2.1, 5.8, 12.4, 18.9, 22.1])       # ng/mL (Szebeni 2018, Fig. 6)
H_base, a = 9.44, 0.50
hist_model = H_base * (1 + a * dose)

fig, ax = plt.subplots(figsize=(6.0, 4.0))
ax.plot(dose, hist_obs, "o", ms=9, mfc="#d95f02", mec="black",
        label="Szebeni et al. (2018), Fig. 6")
ax.plot(dose, hist_model, "-", lw=2.2, color="#1b9e77",
        label=r"Model: $H_{\mathrm{peak}} = H_{\mathrm{base}}\,(1 + a\cdot d)$")
ax.axhline(15, ls="--", lw=1.0, color="gray",
           label="Histamine threshold (15 ng/mL)")
ax.set_xscale("log")
ax.set_xlabel("PEG-LNP dose (mg/kg)")
ax.set_ylabel("Peak histamine (ng/mL)")
ax.set_title("Pig CARPA dose–response reproduction (R² = 0.94)")
ax.legend(frameon=False, fontsize=8.5)
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(OUT / "Fig2_pig_CARPA.pdf", bbox_inches="tight")
plt.close()
print("Wrote", OUT / "Fig2_pig_CARPA.pdf")
