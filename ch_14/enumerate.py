foo = [1, 10, 13, 24, 36, 38, 48, 52]

for i, n in enumerate(foo):
    print(i, n)


j = 0
for n in foo:
    print(j, n)
    j = j + 1


for entry in enumerate(foo):
    print(entry)