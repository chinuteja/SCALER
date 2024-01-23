
## Time complexit O(N*log(log(N)))

def prime_numbers(N):
    primes = []
    for i in range(N+1):
        primes.append(True)
    primes[0] = False
    primes[1] = False
    for i in range(2,N+1,1):
        if (primes[i] == True):
            j = 2*i

            while (j<=N):
                primes[j] = False

                j += i

    for i in range(len(primes)):
        if primes[i] == True:
            print(i)
prime_numbers(7)