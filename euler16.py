"""


2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import time
start_t = time.time()

def get_sum(num, exp):
    mult = num ** exp
    string_num = str(mult)
    sum = 0
    for i in range(0, len(string_num)):
        sum += int(string_num[i])
    return sum
print("ans:",get_sum(2,1000),"\ntime:", time.time() - start_t)