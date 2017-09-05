"""


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time
import lib_fun as lib
start_t = time.time()

def get_largest_prime_factor(num):
    prime_factors = lib.get_prime_factors(num)
    prime_factors = list(set(prime_factors))
    prime_factors.sort()
    return prime_factors[-1:]

if __name__ == '__main__':
    answer = get_largest_prime_factor(600851475143)
    print("Answer:",answer, " time:", time.time() - start_t)
    