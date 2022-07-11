def factorial(number: int) -> int:
    if number == 0:
        return 1
    f=1
    for i in range(1, number + 1):
         f = f * i
    return f

def digits_sum(number: int) -> int:
    if number >= 1000000000:
        return 0
    digits_s = 0
    while number != 0:
        digits_s = digits_s + factorial(number % 10)
        number = number // 10
        
