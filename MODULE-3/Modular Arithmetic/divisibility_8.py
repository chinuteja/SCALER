def solve(A):


    ans = 0
    p = 8
    if len(A) == 1:

        ans = int(A)%p
    if len(A) == 2:
        ans = int(A)%p
    else:
        number = A[(len(A)-3):]
        ans = int(number)%p
    if ans == 0 :
        return 1
    return 0
print(solve("123"))


        