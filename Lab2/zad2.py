import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris.csv")

#numeryczne kolumny
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
#piąta kolumna, z gatunkiem
all_classes = df['variety'].values

#podzial na zbior testowy i treningowy (+ podzial na klasę i numeryczne)
(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

#stworzenie modelu i wytrenowanie
drzewo = DecisionTreeClassifier()
drzewo.fit(train_inputs, train_classes)

#wyswietlanie drzewa (zapisanie w pliku tree.eps)
plt.figure()
tree.plot_tree(drzewo)
plt.savefig('tree.eps',format='eps',bbox_inches = "tight")

#dokladnosc modelu na zbiorze testowym
dokladnosc = drzewo.score(test_inputs, test_classes)
print(dokladnosc)

#predict pokazuje zgadniete nazwy irysow
test_zgadniete = drzewo.predict(test_inputs)

macierz_bledow = confusion_matrix(test_classes, test_zgadniete)
print(macierz_bledow)