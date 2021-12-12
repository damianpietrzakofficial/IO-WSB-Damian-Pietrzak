# 1 sposób z wykorzystanie listy

nieparzyste = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
total = sum(nieparzyste)
print(total)

# 2 sposób z wykorzystaniem pętli

s = 0
for i in range(1, 40, 2):
    s = s + i
print(s)

