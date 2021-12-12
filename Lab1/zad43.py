import numpy as np

print("pkt a")

x = np.array([3, 8, 9, 10, 12])
y = np.array([8, 7, 7, 5, 6])

suma_macierzy = x + y
iloczyn_macierzy = x * y
print("Suma macierzy x i y wynosi:", suma_macierzy)
print("Iloczyn macierzy x i y wynosi:", iloczyn_macierzy)

print("pkt b")

print("Iloczyn skalarny macierzy x i y wynosi:", np.dot(suma_macierzy, iloczyn_macierzy))

print("pkt c")

dist = np.sqrt(np.sum(np.square(x)))

print("Długość Euklidesowa wektora x wynosi:", str(round(dist, 2)))

print("pkt d")

x = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
y = np.array([[1, 2, 1],[2, 4, 6], [7, 2, 5]])

iloczyn_macierzowy = np.dot(x,y)
print("Iloczyn macierzowy wynosi:", iloczyn_macierzowy)

print("pkt e")

w = np.random.randint(0,100,(1,50))

print(w)

print("pkt f")

srednia = np.average(w)
minimalna = np.min(w)
maksymalna = np.max(w)
odchylenie_standardowe = np.std(w)

print("Średnia liczb wynosi:", int(srednia))
print("Minimalna liczba wynosi:", int(minimalna))
print("Maksymalna liczba wynosi:", int(maksymalna))
print("Odchylenie standardowe wynosi:", int(odchylenie_standardowe))

print ("pkt g")

x=[]
for i in range(w.shape[1]):
    o = (w[0, i]-(np.min(w)))/(np.max(w)-np.min(w))
    x.insert(i, o)

print("wektor ",x)







