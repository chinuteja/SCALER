def solve(A):
    A.sort()
    N = len(A)
    common_diff = A[0] - A[1]
    for i in range(N-1):
        diff = A[i] - A[i+1]
        if diff != common_diff:
            return 0
        
    
    return 1

def main():
    A = [2, 4, 1]
    print(solve(A))
if __name__ == '__main__':
    main()
