'''
There are A people standing in a circle. 
Person 1 kills their immediate clockwise neighbour and pass the knife to the next person 
standing in circle. This process continues till there is only 1 person remaining. 
Find the last person standing in the circle.

'''


def nearest_power_two(n):

    while (n != 1):
        if n%2 != 0:
            return False
        n = n//2
    return True
def solve(A):

    max_power_two = 0
    for i in range(1,A+1):
        if nearest_power_two(i):

            max_power_two = i
    
    no_kills = A - max_power_two
    knife = (1+(2*no_kills))
    return knife
print(solve(5))