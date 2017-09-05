import time
start_t = time.time()
def get_sum(num):
    sum = 0
    for i in range(1,num):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

if __name__ == '__main__':
    answer = get_sum(1000)
    print("Answer:", answer, " time:", time.time() - start_t)