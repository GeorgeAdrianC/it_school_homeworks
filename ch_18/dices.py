import random

counter = {}
for j in range(1000):
    sum = random.randint(1,6) + random.randint(1,6)
    counter.setdefault(sum, 0)
    counter[sum] = counter[sum] + 1
print(counter)
