
'''
Given an integer array A, find if an integer p exists in the array such that the number 
of integers greater than p in the array equals p.

'''

def solve(A):
    N = len(A)
    A = sorted(A,reverse=True)

    for i in range(0,N):
        if i == 0:
            if A[0] == 0:
                count = 0
        elif (A[i] == A[i-1]):
            pass
        else:
            count = i
        if count == A[i]:
            return 1
    return -1
def main():
    A = [3, 2, 1, 3]
    # A = [1, 1, 3, 3]
    A = [-1,-2,0,0,0,-3]
    # A = [-4,-2,0,-1,-6]
    print(solve(A))

if __name__ == '__main__':
    main()