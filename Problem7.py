#Problem7.py
#Project Euler problem 7
#Addy Duering
#3/8/26
#Lab 7
# My approach is to make a list of prime numbers and add to it until I have 10,001 primes. 
# Then I will print the last one in the list.
from NumberTests import isPrime
from NumberTests import addNum

def main():
    primes = []
    for i in range(2, 200000):
        if isPrime(i):
            addNum(primes, i)
            if len(primes) == 10001:
                print(primes[10000])
                break  

if __name__ == '__main__':
    main() 