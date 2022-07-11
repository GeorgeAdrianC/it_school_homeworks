from __future__ import barry_as_FLUFL


foo = 13
bar = 2 

def foo_squared():
    return foo ** 2

def add_bar():
    bar = 15
    return foo + bar

def multiply_baz():
    baz = 5
    return foo * baz * bar  

print(foo)
print(foo_squared())
print(add_bar())
print(multiply_baz())

