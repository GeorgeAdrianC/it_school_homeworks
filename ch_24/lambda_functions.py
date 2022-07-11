def a_classic(n):
    return n + 100

def another_classic(m, n, p):
    return m * n + p

a_lambda = lambda n: n + 100

another_lambda = lambda m, n, p: m * n + p

print(a_classic(1))
print(a_lambda(1))

print(another_lambda(10, 10, 5))



f = lambda x: x[0]