def moja_funkcja():
    print("Moja funkcja")
    print("coś wypisuje")

def dzialanie(a, b):
    S = a + b
    I = a * b
    D = a / b
    return [S, I, D]

moja_funkcja()
moja_funkcja()

wynik = dzialanie(10,5)
print(wynik)