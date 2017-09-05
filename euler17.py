"""


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""
import time
start_t = time.time()
num_dic = {0:"",1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
            11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
            30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"one thousand"}
def get_words(num):
    word =""
    #print("Converting:",num)
    if num == 1000 or num <= 20:
        return num_dic.get(num)
    if num > 20 and num < 100:
        tens_place = (num // 10) * 10
        #print("ck1:",num_dic.get(tens_place) ," ", num_dic.get(num%10))
        return num_dic.get(tens_place) +" "+ num_dic.get(num%10)
    else:
        if num % 100 == 0:
            #print("ck2:",num_dic.get(num // 100), " hundred")
            return num_dic.get(num // 100) + " hundred"
        else: 
            hundreds = num // 100
            #print("ck3:",num_dic.get(hundreds) , " hundred and " , get_words(num % 100))
            return num_dic.get(hundreds) + " hundred and " + get_words(num % 100)
total_len = 0
for i in range(1, 1001):
    word = get_words(i)
    words = word.split()
    len_w = 0
    for w in words:
        len_w += len(w)
    total_len += len_w
print("Ans:",total_len,"\nTime:",time.time() - start_t)