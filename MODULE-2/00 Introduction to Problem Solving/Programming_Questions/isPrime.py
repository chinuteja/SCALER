import math
def isPrime(A):
    count = 0
    for i in range(1,int(math.sqrt(A))+1):
        if (A%i) == 0:
            count = count + 2
    if count == 2:
        return True
    return False

def solve(N):
    final_count = 0
    for i in range(2,N+1):
        if isPrime(i):
            # print(i)
            final_count += 1
    return final_count

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()
