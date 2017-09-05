"""


n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
import time
start_t = time.time()

def get_factorial(num):
    if num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)
num = get_factorial(100)
sum = 0
num_str = str(num)
for i in range(0,len(num_str)):
    sum += int(num_str[i])
print("ans:", sum," time:", time.time() - start_t)