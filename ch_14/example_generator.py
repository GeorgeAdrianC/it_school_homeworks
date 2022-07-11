def gen():
    for i in range(0, 5):
        yield i**2

g = gen()

foo = next(g)
print(foo)

bar = next(g)
print(bar)

name = input("Please type your name: ")

baz = next(g)
print(baz)

baz = next(g)
print(baz)

f = gen()

l = list(gen())

print(l)