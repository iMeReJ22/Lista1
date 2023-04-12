k = int(input("Podaj k: "))
while True:
    co = input("Slownik czy lista (s/l): ")
    if co == "s":
        out = {}
        break
    if co == "l":
        out = list()
        break

for i in range(20, 81):
    if i % k == 0:
        if type(out) == list:
            out.append(i)
        else:
            out[i] = i

print(out)
