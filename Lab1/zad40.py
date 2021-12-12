print("Podaj bok trójkąta:")
bok = (int(input()))
poziom = bok * "x"

for i in range(bok):
    wiersz = (bok - (bok -i)) * "x"
    spacje = (bok - i) * " "
    print(spacje+wiersz)
print(poziom)

print("Podaj bok trójkąta:")
bok = (int(input()))
poziom = bok * "x"

for i in range(bok):
    wiersz = (bok - (bok -i)) * "x"
    spacje = (bok - i) * " "
    print(spacje+wiersz)
print(poziom)