a = 2
b = 1
c = 3

if a == b:
    if b == c:
        print("Wszystkie liczby, a, b, c, są sobie równe")
    else:
        print("Liczby a i b są równe")
elif a == c:
    if b == c:
        print("Wszystkie liczby, a, b, c, są sobie równe")
    else:
        print("Liczby a i c są równe")
elif b == c:
    if a == c:
        print("Wszystkie liczby, a, b, c, są sobie równe")
    else:
        print("Liczby b i c są równe")
else:
    print("Nie ma pary równych liczb")





