def is_prime(number):
    # Check whether or not a number is prime
    # i.e. does it have any factors other than itself and one?
    if number == 1:
        return False
    factor = 2
    checked = set()
    while factor**2 <= number:
        if number % factor == 0:
            return False
        factor += 1
    return True
        

def kth_multiple_357(k):
    ctr = 0
    num = 0
    primes_under_num = []
    while ctr < k:
        num += 1
        if is_prime(num) and num not in [3, 5, 7]:
            primes_under_num.append(num)
        else:
            flag = 0
            for prime in primes_under_num:
                if num % prime == 0:
                    flag = 1
                    break
            if not flag: 
                ctr += 1

    return num

def test_case(k, solution, test_func):

    output = test_func(k)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case(7, 21, kth_multiple_357)


