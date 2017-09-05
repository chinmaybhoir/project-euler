"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
from itertools import permutations
start_t = time.time()

num_string = "0123456789"
string_perms = ["".join(p) for p in permutations(num_string)]
num_perms = [int(num) for num in string_perms]
answer = num_perms[1000000 - 1]
print("ans:", answer," time:", time.time() - start_t)