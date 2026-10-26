KM_FACTORS = {'Mouse': 3, 'Rat': 6, 'Macaque': 12, 'Human': 37}


def human_equivalent_dose(dose_mg_kg, species):
	return dose_mg_kg * (KM_FACTORS[species] / KM_FACTORS['Human'])
