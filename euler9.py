"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

NOTE: this problem is solved by naive method. There exists even more interesting method, by using Euler's formula for
Pythagorean triplet

"""
import time
start_t = time.time()
def get_triplet_prod(num):
    for a in range(1,num):
        for b in range(1, num-1):
            c = num - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

if __name__ == '__main__':
    answer = get_triplet_prod(1000)
    print("ans:", answer, " time:", time.time() - start_t)
    