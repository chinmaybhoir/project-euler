"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import time
import numpy as np
import lib_fun as lib
start_t = time.time()
'''
def is_prime(num):
    for i in range(2,int(np.sqrt(num) + 1)):
        if num%i == 0:
            return False
    return True
'''
def get_sum(num):
    sum = 0
    for i in range(2,num):
        if lib.is_prime(i):
            sum += i
    return sum

if __name__ == '__main__':
    print("ans:",get_sum(2000000))
    print("time taken:",time.time() - start_t)