
def jos(N):

	## if N is power of 2 then last man standing is going to be answer
	## observation
	## find closet power of 2 < N find no of kills (N-CP) ans = 1+(2*kills)

	closet_power = 1
	while closet_power < N:
		closet_power  = closet_power * 2
	if closet_power == N:
		closet_power = closet_power
	else:
		closet_power = closet_power//2
	no_kills = N - closet_power
	return 1 + (2*no_kills)
N = 1
N = 4
N = 8
N = 9
N = 15
print(jos(N))