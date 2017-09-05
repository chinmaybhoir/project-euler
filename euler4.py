"""


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
import time
start_t = time.time()

def is_palindrome(num):
    num_string = str(num)
    if num_string == num_string[::-1]:
        return True
    return False

def get_palindrome():
    largest = 0
    for i in range(101,1000):
        for j in range(101, 1000):
            if is_palindrome(i*j) and i*j > largest:
                largest = i * j
    return largest

if __name__ == '__main__':
    answer = get_palindrome()
    print("ans:", answer, " time:", time.time() - start_t)