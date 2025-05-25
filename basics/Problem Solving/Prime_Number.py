def prime_numbers():
    # Get user input
    number = int(input("Enter a number: "))
    # Check if the number is prime
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

        return None
prime_numbers()