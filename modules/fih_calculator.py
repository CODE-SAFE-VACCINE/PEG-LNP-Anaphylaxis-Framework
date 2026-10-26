HISTAMINE_THRESHOLD = 15.0
SAFETY_MARGIN = 10.0


def fih_dose(model, safety_margin=SAFETY_MARGIN):
	max_dose = HISTAMINE_THRESHOLD / (model['H_base'] * (1 + model['a']))
	return max_dose / safety_margin
