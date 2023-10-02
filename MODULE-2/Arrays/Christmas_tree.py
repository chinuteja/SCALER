'''
You are given an array A consisting of heights of Christmas trees and an array B of the same size 
consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), 
and you are supposed to choose 3 trees (let's say, indices p, q, and r), 
such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.
You are to choose 3 trees such that their total cost is minimum. Return that cost.
If it is not possible to choose 3 such trees return -1.

Input :
 A = [1, 3, 5]
 B = [1, 2, 3]
 Output :
  6 

We can choose the trees with indices 1, 2 and 3, and the cost is 1 + 2 + 3 = 6. 

'''

def bruteforce():
    '''
    Time complexity O(N**3)
    Space complexity O(N)
    '''
    minimum_cost = []
    A = [2,4,5,4,10]
    B = [40,30,20,10,40]
    for p in range(len(A)):
        for q in range(p+1,len(A)):
            for r in range(q+1,len(A)):
                if (A[p]<A[q]<A[r]):
                    cost = B[p] + B[q] + B[r]
                    minimum_cost.append(cost)

    if len(minimum_cost) == 0:
        return -1
    return min(minimum_cost)

print(bruteforce())