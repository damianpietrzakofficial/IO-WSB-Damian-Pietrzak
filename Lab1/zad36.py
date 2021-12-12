print("Podaj boki prostokąta a i b:")
bok1 = input()
bok2 = bok1.split()
a = int(bok2[0])
b = int(bok2[1])

if (a <= 0) or (b <= 0):
    print("Nieprawidłowe dane")
else:
    P = a * b
    L = 2 * a + 2 * b
    print("Pole prostokąta P =",P, "a obwód L =",L)



