import numpy as np
import time
start_t = time.time()
str_pyramid = open("p067_triangle.txt")
def ret_max(num, arr, i):
    return num + np.maximum(arr[i],arr[i+1])
string = str(str_pyramid)
pyramid_lines_str = []
for line in str_pyramid:
    pyramid_lines_str.append(line)
pyramid_lines = []
for line in pyramid_lines_str:
    digits = line.split()
    temp_arr = []
    for digit in digits:
        temp_arr.append(int(digit))
    pyramid_lines.append(temp_arr)
index = 0
temp_modified_arr = np.zeros((10,10))
for i in range(len(pyramid_lines) - 1,0,-1):
    line = pyramid_lines[i-1]
    if i == len(pyramid_lines) - 1:
        arr = pyramid_lines[i]
    else:
        arr = temp_modified_arr[0]
    index = 0
    temp_modified_arr = np.zeros((len(line),len(line)))
    for num in line:
        modified_list = ret_max(num, arr, index)
        temp_modified_arr[0][index] = modified_list
        index += 1
print("Ans:",modified_list," time:",time.time() - start_t)