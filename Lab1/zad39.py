print("Podaj bok trójkąta:")
bok = (int(input()))
poziom = bok * "x"

for i in range(bok):
    wiersz = (bok - (bok -i))*"x"
    print(wiersz)
print(poziom)