import sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[0]).resolve().parents[1]))
import numpy as np
from modules.monte_carlo import MODEL_PEG

dose = np.array([0.01, 0.03, 0.10, 0.30, 1.00])
hist = np.array([2.1, 5.8, 12.4, 18.9, 22.1])
pred = MODEL_PEG['H_base'] * (1 + MODEL_PEG['a'] * dose)
ss_res = np.sum((hist - pred) ** 2)
ss_tot = np.sum((hist - hist.mean()) ** 2)
print('Pig CARPA reproduction: R^2 = %.3f' % (1 - ss_res / ss_tot))
