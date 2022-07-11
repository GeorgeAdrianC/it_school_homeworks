def inverse(number: int) -> int:
    inv = 0
    while number !=0:
        inv = (inv * 10) + (number % 10)
        number = number // 10
    return inv
print(inverse(123456789))