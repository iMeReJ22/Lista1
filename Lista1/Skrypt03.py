a = 3
b = 4
for i in range(a):
    for j in range(b):
        print("*", end="")
    print()

pole = a*b
obwod = 2*a + 2*b
print(f"Pole: {pole}\nObwód: {obwod}")
