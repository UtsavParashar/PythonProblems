from concurrent.futures import ProcessPoolExecutor
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n %2 == 0:
        return False
    
    for val in range(3, math.floor(math.sqrt(n))+1, 2):
        if n % val == 0:
            return False
    return True

def main():
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is {prime}')

if __name__ == '__main__':
    main()
        