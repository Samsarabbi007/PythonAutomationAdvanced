def prime_numbers_in_interval(start, end):
    """
    This function takes a start and end number and returns a list of all prime numbers in that interval.
    """
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(prime_numbers_in_interval(10, 50))