
def smallest_prime_factor(N):
	spf = []
	for i in range(N):
		spf.append(i)

	for i in range(2,N+1):

		if (spf[i] == i):

			j = 2*i

			while (j<=N):
				spf[j] = min(spf[i],j)

				j = j + i