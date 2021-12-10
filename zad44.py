import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
print("pkt a")
df = pd.read_csv('miasta.csv')
print(df)

print("pkt b")
rok_2010 = {'Rok': 2010, 'Gdansk': 460, 'Poznan': 555, 'Szczecin': 405}
df1 = df.append(rok_2010, verify_integrity=True, ignore_index=True)

print(df1)

# pkt c
xpoints = np.array([1900, 1925, 1939, 1946, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
ypoints = np.array([170, 210, 250, 117, 194, 286, 365, 456, 465, 462, 460])
ypoints1 = np.array([110, 220, 274, 267, 320, 408, 471, 552, 590, 574, 555])
ypoints2 = np.array([210, 254, 287, 72, 178, 269, 338, 388, 413, 416, 405])

plt.plot(xpoints, ypoints, marker = 'o', color = 'r')
plt.plot(xpoints, ypoints1, marker = 'o', color = 'g')
plt.plot(xpoints, ypoints2, marker = 'o', color = 'y')
plt.title("Ludność w miastach Polski")
plt.ylabel("Licza ludności w tys.")
plt.xlabel("Lata")
plt.show()