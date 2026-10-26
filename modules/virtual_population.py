import numpy as np
import pandas as pd


def build_virtual_population(n=1000, seed=42):
	rng = np.random.default_rng(seed)
	titres = []
	for _ in range(n):
		r = rng.random()
		if r < 0.30:
			titres.append(0.0)
		elif r < 0.80:
			titres.append(rng.lognormal(0, 0.5))
		else:
			titres.append(rng.lognormal(0, 0.6))
	return pd.DataFrame({'titre': titres})
