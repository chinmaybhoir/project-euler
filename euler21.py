"""


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
import time
start_t = time.time()
def ret_divisors(num):
    divisors = []
    for i in range(1,num//2 + 1):
        if num%i == 0:
            divisors.append(i)
    return divisors

def sum_divisors(num):
    divisors = ret_divisors(num)
    sum = 0
    for num in divisors:
        sum += num
    return sum

def get_amicable_nums(upper_limit):
    amicable_nos = []
    for i in range(1, upper_limit):
        divisors_sum = sum_divisors(i)
        if divisors_sum != i:
            second_num = divisors_sum
            divisors_sum_second = sum_divisors(second_num)
            if divisors_sum_second == i and (divisors_sum_second not in amicable_nos) and (i not in amicable_nos):
                amicable_nos.append(i)
                amicable_nos.append(second_num)
    return amicable_nos

if __name__ == '__main__':
    amicable_nos = get_amicable_nums(10000)
    print("amicable nos:",amicable_nos)
    sum = 0
    for num in amicable_nos:
        sum += num
    print("ans:", sum," time:", time.time() - start_t)
