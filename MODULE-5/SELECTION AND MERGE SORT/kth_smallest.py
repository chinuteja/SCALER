def kthsmallest(A, B):
    A = list(A)

    A.sort()
    # print(A)
    if B == 1:
        return A[0]
 

    return A[B-1]


A = [94,87,100,11,23,98,17,35,43,66,34,53,72,80,5,34,64,71,9,16,41,66,96]

B = 19
print(kthsmallest(A,B))