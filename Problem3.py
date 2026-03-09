#Problem3.py
#Project Euler problem 3
#Addy Duering
#3/8/26
#Lab 7
# My approach is to make a function that tests the factors with my 
# isPrime function and filters them to find the largest.

from NumberTests import isPrime

def find_largest_prime_factor(n):
    """Find the largest prime factor of n."""
    largest_prime = 1
    
    # Check for 2
    if n % 2 == 0:
        if isPrime(2):
            largest_prime = 2
        while n % 2 == 0:
            n //= 2
    
    # Check odd factors
    i = 3
    while i * i <= n:
        if n % i == 0:
            if isPrime(i):
                largest_prime = i
            while n % i == 0:
                n //= i
        i += 2
    
    # If n is a prime number greater than 2
    if n > 1 and isPrime(n):
        largest_prime = n
    
    return largest_prime

def main():
    number = 600851475143
    result = find_largest_prime_factor(number)
    print(f"The largest prime factor of {number} is {result}")

if __name__ == '__main__':
    main()