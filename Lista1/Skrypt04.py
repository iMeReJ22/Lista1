cenyPrzed = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
cenyPo = [4.5, 5.5, 4.69, 4.99, 4.00]

print(f"Max po: {max(cenyPo)}")

print(f"Min ogólnie: {min(min(cenyPrzed), min(cenyPo))}")

print(f"Średnia przed: {sum(cenyPrzed) / len(cenyPrzed)}")

print(f"Średnia po: {sum(cenyPo) / len(cenyPo)}")
