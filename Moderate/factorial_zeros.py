def factorial(num):
    if 0 <= num <= 1:
        return 1
    return num * factorial(num - 1) 

def factorial_zeros(num):
    f = factorial(num)
    zeros = 0
    while f >= 10:
        f /= 10
        zeros += 1
    return zeros

print(factorial_zeros(13))
