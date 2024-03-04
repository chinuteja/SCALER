'''
Given an array of integers A, of size N.

Return the maximum size subarray of A having only 
non-negative elements. 
If there are more than one such subarray, 
return the one having the smallest starting index in A.
 A = [5, 6, -1, 7, 8]
Ouptut = [5,6]
'''



class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Tarun
    def solve(self, A):
        maxCountSoFar = 0
        start = 0
        end = 0
        s = 0
        count = 0

        for i in range(len(A)):
            if A[i] >= 0:
                count += 1
            if maxCountSoFar < count:
                maxCountSoFar = count
                start = s
                end = i
            if A[i] < 0:
                s = i + 1
                count = 0

        return A[start:end + 1]
def max_non_negative_subarray(A):
    n = len(A)  # Get the length of the input array A
    max_len = 0  # Initialize the maximum subarray length
    current_len = 0  # Initialize the current subarray length
    start_index = 0  # Initialize the starting index of the current subarray
    max_start = 0  # Initialize the starting index of the maximum subarray

    for i in range(n):  # Iterate through each element in the array
        if A[i] >= 0:  # Check if the current element is non-negative
            current_len += 1  # Increment the current subarray length
        else:
            current_len = 0  # Reset the current subarray length to zero
            start_index = i + 1  # Update the starting index for the new subarray

        if current_len > max_len:  # Check if the current subarray is longer than the maximum subarray
            max_len = current_len  # Update the maximum subarray length
            max_start = start_index  # Update the starting index of the maximum subarray

    return A[max_start: max_start + max_len]  # Return the maximum subarray based on the starting index and length

# Example usage:
A = [1, 2, -1, 3, 4, 10, 0, -1, 8]  # Example input array
result = max_non_negative_subarray(A)  # Call the function with the example array
print(result)  # Print the result


A = [5, 6, -1, 7, 8]
A = [5, 6, -1, 7, 8,9]
A =  [1, 2, 3, 4, 5, 6]
A = [-6148706,-8550681,4494391,8074193,-1283236,4384884,8111626,-8972065,7428432,7514578]
sol = Solution()
# print(sol.solve(A))
print(max_non_negative_subarray(A))