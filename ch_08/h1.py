n = int(input("Enter your number: "))
maxim = -1
while n > 0:
    c = n % 10 
    if maxim < c:
        maxim = c
   
    n=n//10
print(format(maxim, ".2f"))
       
