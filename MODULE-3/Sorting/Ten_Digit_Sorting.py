from functools import cmp_to_key


def comparator(a,b):
    a_1 = (a//10)%10
    b_1 = (b//10)%10

    if a_1 < b_1:
        return -1
    if a_1 > b_1:
        return 1
    if a_1 == b_1:
        if a < b:
            return 1
        if a > b:
            return -1
        else:
            return 0
def solve(A):
    # A = sorted(A)
    sorted_arr = sorted(A, key=cmp_to_key(comparator))
    return sorted_arr
A = [15, 11, 7, 19]
print(solve(A))