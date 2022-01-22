import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("diabetes.csv")

#kolumny z parametrami
all_inputs = df[["pregnant-times", "glucose-concentr", "blood-pressure", "skin-thickness", "insulin", "mass-index", "pedigree-func", "age"]].values

#kolumna z klasą
all_classes =  df["class"].values

#podział na zbiory testowy i treningowy oraz na klasę numeryczną
(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size = 0.7, random_state = 1)

#tworzenie drzewa i wygenerowanie
dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)

#wyświetlenie drzewa i zapisanie w pliku eps
plt.figure()
tree.plot_tree(dtc)
plt.savefig("diabetes_drzewo.eps", format = "eps", bbox_inches = "tight")

#dokładność modelu na zbiorze testowym
dokladnosc = dtc.score(test_inputs, test_classes)
print(dokladnosc)

#predict pokazuje odgadnięte prawidłowo
test_zgadniete = dtc.predict(test_inputs)

#macierz błędu
cf = confusion_matrix(test_classes, test_zgadniete)
print(cf)

# bez wykresu słupkowego, nie udało mi się go zrobić prawidłowo



