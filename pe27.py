"""
Problem 27
==========


   Euler discovered the remarkable quadratic formula:

                                  n² + n + 41

   It turns out that the formula will produce 40 primes for the consecutive
   values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
   is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
   divisible by 41.

   The incredible formula  n² − 79n + 1601 was discovered, which produces 80
   primes for the consecutive values n = 0 to 79. The product of the
   coefficients, −79 and 1601, is −126479.

   Considering quadratics of the form:

     n² + an + b, where |a| < 1000 and |b| < 1000

     where |n| is the modulus/absolute value of n
     e.g. |11| = 11 and |−4| = 4

   Find the product of the coefficients, a and b, for the quadratic
   expression that produces the maximum number of primes for consecutive
   values of n, starting with n = 0.

   
   Answer: 69d9e3218fd7abb6ff453ea96505183d

"""
import math
import sys
import time

START_T = time.time()

def is_prime(num):
    for i in range(2,int(math.sqrt(num) + 1)):
        if num%i == 0:
            return False
    return True

MAX_COUNT = 0
MAX_A = 0
MAX_B = 0

def get_eq(a, b, n):
  return n**2 + a*n + b

def get_prime_count(a, b):
  prime_count = 0
  for n in range(0,abs(b)+1):
    if (b != 0 and n%abs(b) == 0) and (not is_prime(abs(b))):
      break
    num = get_eq(a, b, n)
    if num > 0 and is_prime(num):
      prime_count += 1
    else:
      break
  return prime_count

if __name__ == '__main__':
  a = -999
  b = -999
  while a < 1000:
    b = -999
    while b < 1000:
      prime_count = get_prime_count(a, b)
      if prime_count > MAX_COUNT:
        MAX_COUNT = prime_count
        MAX_A = a
        MAX_B = b
      b +=1
    a += 1

  print("count:", MAX_COUNT)
  print("a:", MAX_A, "b:", MAX_B)
  print("t:",time.time() - START_T)

