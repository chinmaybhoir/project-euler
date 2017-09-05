# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:09:55 2017

@author: Chinmay.Bhoir
"""

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime 
is 13.

What is the 10 001st prime number?
"""

import time
start_t = time.time()
import numpy as np
import lib_fun as lib

def get_nth_prime(n):
    prime_count = 0
    for i in range(2,99999999999):
        if lib.is_prime(i):
            prime_count += 1
        if prime_count == n:
            answer = i
            break
    return answer
if __name__ == '__main__':
    print(get_nth_prime(10001))
    print(time.time() - start_t)
