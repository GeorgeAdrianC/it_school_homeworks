n = int(input("How many numbers are in your list: "))
v = [0 for i in range(n)]

for i in range(n):
    v[i] = int(input("Current number: "))

print(v)

for i in range(n):
    for j in range(i + 1, n):
        if v[i] < v[j]:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux

print(v)