import random
from datetime import datetime

gracze ={}
for i in range(10):
    gracze[f"Gracz{i+1}"] = [{datetime.now().strftime("%D"): random.randint(0, 100)}]

print(gracze)