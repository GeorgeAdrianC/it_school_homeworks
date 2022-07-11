def factorial(number: int):
    if number == 0:
        return 1

    f = 1 

    for i in range(1, number +1):
        f = f * i
    return f

print(factorial(69369))
