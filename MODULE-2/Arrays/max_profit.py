#Question-1
# A = [3,5,7,2,4,3,8,6]
# A = [1,2]
# max_profit = 0
# N = len(A)
# max_ = A[N-1]
# for i in range(N-2,-1,-1):
#     if A[i] > max_:
#         max_ = A[i]
#     profit = max_-A[i]
#     if profit > max_profit:
#         max_profit = profit
# print(max_profit)

#Question - 3

A = "ABEC"
count_vowel,answer = 0,0
A = A.lower()
for i in range(len(A)):
    if A[i] in ["a","e","i","o","u"]:
        count_vowel  = count_vowel + len(A) - i

print(count_vowel)



output = []
A = [16,17,4,3,5,2]
N = len(A)
for i in range(N-1):
    intial_leader = A[i]
    for j in range(i+1,N):
        if intial_leader < A[j]:
            intial_leader = A[j]
    output.append(intial_leader)
output.append(A[N-1])
print(list(set(output)))




def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        sell = sell + 1
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))