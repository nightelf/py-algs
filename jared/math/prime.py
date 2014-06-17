__author__ = 'jared'
import math



def isPrime1(number):

    if not isinstance(number, int):
        raise ValueError('First parameter must be integer.')

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def isPrime2(number):

    if not isinstance(number, int):
        raise ValueError('First parameter must be integer.')

    if number < 2:
        return False
    elif number in [2, 3]:
        return True
    elif (number * number - 1) % 24 != 0:
        return False
    else:
        return isPrime1(number)

def testIsPrime(prime_func):

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(101):
        if i in primes:
            assert prime_func(i) == True, 'Number %d is not prime, but is calculated as prime.' % i
        else:
            assert prime_func(i) == False, 'Number %d is prime, but is calculated as not prime.' % i

# testIsPrime(isPrime1)
# testIsPrime(isPrime2)

