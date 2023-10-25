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

Input :
    A = [1, 6, 4, 2, 6, 9]
 B = [2, 5, 7, 3, 2, 7]
  We can choose the trees with indices 1, 4 and 5, and the cost is 2 + 3 + 2 = 7. 
 This is the minimum cost that we can get.

We can choose the trees with indices 1, 2 and 3, and the cost is 1 + 2 + 3 = 6. 

'''
 def solve(self, A, B):
        mincost=sys.maxsize
        n=len(A)
        m=len(B)
        for i in range(1,n-1):
            Lcost=sys.maxsize
            Rcost=sys.maxsize
            for j in range(i-1,-1,-1):
                if A[j]<A[i]:
                    Lcost=min(Lcost,B[j])
            for k in range(i+1,n):
                if A[k]>A[i]:
                    Rcost=min(Rcost,B[k])
            mincost=min(mincost,Lcost+Rcost+B[i])
        if mincost==sys.maxsize:
            return -1
        return mincost

def optimized(A,B):
    final_ans = []
    n = len(A)
    req_left_index,req_right_index = 0,0
    for q in range(1,n-1):
        A_q = A[q]
        p = q-1
        while(p>=0):
            A_p = A[p]
            
            if A_p < A_q:
                # print("A_p ",A_p,A_q)
                req_left_index = p
                print("req_left_index",req_left_index)
            p = p -1
            
                
        for r in range(q+1,n):
            A_r = A[r]
            if A_q < A_r:
                req_right_index = r
                print("req_right_index ",r)
        final_ans.append(B[req_left_index]+B[q]+B[req_right_index])
    return min(final_ans)


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

# print(bruteforce())
A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]
print(optimized(A,B))