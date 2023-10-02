import math
def get_factors(num):


    k = int(math.sqrt(num))
    count = 0
    for i in range(1, k+1):
        if num % i == 0:

            if i == num//i:

                count += 1
            else:
                count += 2
    return count
print(get_factors(100))