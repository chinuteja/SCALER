'''
You are given an array A of length N and Q queries given 
by the 2D array B of size Q*2. Each query consists of two integers B[i][0] 
and B[i][1].

A = [1, 2, 3, 4, 5]

B = [   [0,2] 
        [1,4]   ]
[4, 8]

The subarray for the first query is [1, 2, 3] whose sum of even indices is 4.

The subarray for the second query is [2, 3, 4, 5] whose sum of even indices is 8.

'''

def solve(A,B):

    N = len(A)
    prefix_even = []
    prefix_even.append(A[0])

    for i in range(1,N):
        if i%2 == 0:
            prefix_even.append(prefix_even[i-1] + A[i])
        else:
            prefix_even.append(prefix_even[i-1])


    output = []

    for inner in B:
        start_index = inner[0]
        end_index = inner[1]


        if start_index == 0:
            output.append(prefix_even[end_index])
        else:
            sum_ = prefix_even[end_index] - prefix_even[start_index-1]
            output.append(sum_)
    return output


A = [1, 2, 3, 4, 5]

B = [   [0,2], 
        [1,4]   ]

print(solve(A,B))