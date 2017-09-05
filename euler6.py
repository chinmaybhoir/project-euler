# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:03:21 2017

@author: Chinmay.Bhoir
"""

"""


The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.

"""

import time
import numpy as np 
start_t = time.time()

def get_answer(num):
    squares = np.array([i**2 for i in range(1,101)])
    sum_squares = np.sum(squares)
    nums = np.array([i for i in range(1,101)])
    num_sum =  np.sum(nums)
    num_sum_sq = num_sum ** 2
    diff = num_sum_sq - sum_squares
    return diff

if __name__ == '__main__':
    answer = get_answer(100)
    print("Answer:", answer," time:", time.time() - start_t)
