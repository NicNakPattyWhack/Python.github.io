def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

for n in range(1, 20):
    if is_prime(n):
        print(n, "is prime")
    else: print(n, "is not prime")