print("pkt a")

def obcinaj (s):
    print(s[1:-1])

s = str(input("Podaj dowolny łańcuch symboli: "))

obcinaj(s)

print("pkt b")

a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))
c = int(input("Podaj liczbę c:"))

def max_sum(a,b,c):
    if a >= b and c >= b:
        return(a + c)
    elif b >= a and c >= a:
        return(b + c)
    else:
        return(a + b)

max = max_sum(a, b, c)
print("Suma dwóch największych liczb to:", max)

print("pkt c")

liczby = [20, 4, 7, 3, 19, 37, 28, 4, 2, 14]

def wybierz_parzyste(x):
    for i in range (len(liczby)):
        if liczby[i] % 2 == 0:
            print(liczby[i])

wybierz_parzyste(liczby)

print("pkt d")

a = int(input("Podaj długość podstawy trapezu a: "))
b = int(input("Podaj długośc podstawy trapezu b: "))
h = int(input("Podaj długość wysokości trapezu h: "))

def pole_trapezu(a, b, h):
    pole = ((a + b) * h) / 2
    print("Pole trapezu wynosi: ", pole)

pole_trapezu(a, b, h)