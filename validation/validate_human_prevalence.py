import sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[0]).resolve().parents[1]))
from modules.virtual_population import build_virtual_population

pop = build_virtual_population(1000)['titre'].values
print('negative fraction = %.2f' % (pop == 0).mean())
