x = int(input("Podaj liczbę: "))

for i in range(2, x):
    if x % i == 0:
        print("Podana liczba nie jest liczbą pierwszą")
        break
    else:
        print("Podana liczba jest liczbą pierwszą")
        break
