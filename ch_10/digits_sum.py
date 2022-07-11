def digits_sum(number: int) -> int:
    digits_s = 0
    while number !=0:
        digits_s = digits_s + (number % 10)
        number = number // 10
    return digits_s
print(digits_sum(1234))