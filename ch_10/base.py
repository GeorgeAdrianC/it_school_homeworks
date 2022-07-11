from operator import is_


def base(n: int, b: int) -> bool:
    if n >= 1000000000:
        return False
    if b < 2 or b > 9:
        return False
    
    is_in_base = True
    number_of_operations = 0

    while n != 0:
        number_of_operations += 1
        if n % 10 >= b:
            return False
        n = n // 10
        
    
    return True

print(base(123, 6))