"""


The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import time
start_t = time.time()

fibo_dict  = {}
first = 1
second = 1
num_next = first + second
first = second
second = num_next
index = 4
while True:
    num_next = first + second
    if len(str(num_next)) == 1000:
        print("num:", num_next)
        answer = index
        break
    else:
        first = second
        second = num_next
        index += 1
print("Ans:", answer," time:", time.time() - start_t)
