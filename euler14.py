
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
import numpy as np
start_t = time.time()

def collatz(num):
    node_val = num
    chain_count = 0
    while node_val != 1:
        if node_val%2 == 0:
            node_val /= 2
            chain_count += 1
        else:
            node_val = 3*node_val + 1
            chain_count += 1
    return chain_count
num = 2
longest_chain = 0
required_num = 0
while num < 1000000:
    chain_count = collatz(num)
    if chain_count > longest_chain:
        longest_chain = chain_count
        required_num = num
    num += 1
print("ans:", required_num, "time:", time.time() - start_t)