"""
Problem 30
==========


   Surprisingly there are only three numbers that can be written as the sum
   of fourth powers of their digits:

     1634 = 1^4 + 6^4 + 3^4 + 4^4
     8208 = 8^4 + 2^4 + 0^4 + 8^4
     9474 = 9^4 + 4^4 + 7^4 + 4^4

   As 1 = 1^4 is not a sum it is not included.

   The sum of these numbers is 1634 + 8208 + 9474 = 19316.

   Find the sum of all the numbers that can be written as the sum of fifth
   powers of their digits.

   
   Answer: 27a1779a8a8c323a307ac8a70bc4489d

"""
import time
START_T = time.time()

def get_sum(num,power):
  num_str = str(num)
  sum_num = 0
  for digit in num_str:
    sum_num += (int(digit) ** power)
  return sum_num

def is_reflective(num, power):
  return True if get_sum(num,power) == num else False

if __name__ == '__main__':
  numbers = []
  ans = 0
  upper_bound = 5 * (9**5)
  for i in range(2,upper_bound):
    if is_reflective(i,5):
      ans += get_sum(i,5)
      numbers.append(i)
  print(numbers)
  print(ans)
  print("t:", time.time() - START_T)