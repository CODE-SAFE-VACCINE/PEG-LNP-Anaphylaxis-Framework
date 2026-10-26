import numpy as np

MODEL_PEG = {'H_base': 9.44, 'IL6_base': 45.0, 'a': 0.50, 'b': 0.30}
MODEL_PGL = {'H_base': 1.50, 'IL6_base': 4.00, 'a': 0.02, 'b': 0.01}


def monte_carlo_dose_response(pop, model, dose_mg_kg, n_sims=1000, seed=42):
	rng = np.random.default_rng(seed)
	idx = rng.integers(0, len(pop), n_sims)
	titre = pop['titre'].values[idx]
	h = model['H_base'] * (1 + model['a'] * titre)
	i6 = model['IL6_base'] * (1 + model['b'] * titre)
	return np.column_stack([h, i6])
