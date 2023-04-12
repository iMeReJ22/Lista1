a = int(input("Podaj prog początkowy: "))
b = int(input("Podaj prog koncowy: "))
n = int(input("Podaj ile k: "))
outOut = {}
for i in range(n):
    k = int(input("Podaj k: "))

    out = list()

    for i in range(a, b+1):
        if i % k == 0:
            out.append(i)
    outOut[k] = out

print(outOut)
