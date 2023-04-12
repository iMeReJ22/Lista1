a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Boki nie mogą być mniejsze od zera >:(")
    exit(1)

boki = [a, b, c]

boki = sorted(boki)

a = boki[0]
b = boki[1]
c = boki[2]

if a*a + b*b == c*c:
    print("Trójka jest pitagorejska.")
else:
    print("Trójka nie jest pitagorejska")


