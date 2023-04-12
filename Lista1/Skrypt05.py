import random

gracze ={}
for i in range(10):
    gracze[f"Gracz{i+1}"] = random.randint(0, 100)

print(gracze)