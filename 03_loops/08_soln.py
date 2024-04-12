import math

def isPrime(num):
    if num <=1: 
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)), 2):
            if num % i == 0:
                return False
            else:
                return True

ans = isPrime(12)

if ans == True:
    print("Is Prime number")
else:
    print("Not a Prime number")