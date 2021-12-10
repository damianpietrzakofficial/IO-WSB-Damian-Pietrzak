import pandas as pd
print("pkt a")
df = pd.read_csv('miasta.csv')
print(df)

print("pkt b")
rok_2010 = {'Rok': 2010, 'Gdansk': 460, 'Poznan': 555, 'Szczecin': 405}
df1 = df.append(rok_2010, verify_integrity=True, ignore_index=True)

print(df1)
