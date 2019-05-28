import sys
from math import sqrt

clArgs = sys.argv[1:]
num = int(clArgs[0])


def isNumberPrime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        else:
            i += 1
    return True


if isNumberPrime(num):
    print(f'{num} is Prime!')
else:
    print(f'{num} is not Prime...')

input('Press ENTER to exit')

# Sieve of Eratosthenes is cool and all, but does not make sense to implement it in this problem.  That is, this program is only asked to tell whether or not the number is prime.  The sieve would be an over-calculation for this defined goal.  The sieve is more effectively used to solve a problem asking 'how many prime numbers are between these 2 numbers?'
