def generate_perfect_squares(N):
    perfect_squares = []
    i = 1

    while i*i <= N:
        perfect_squares.append(i*i)
        i += 1

    return perfect_squares

# Example: Generate perfect squares between 1 and 50
N = 50
result = generate_perfect_squares(N)
print(result)
def generate_perfect_squares_binary(N):
    if N < 1:
        return []

    perfect_squares = []
    left, right = 1, N

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square <= N:
            perfect_squares.append(square)
            left = mid + 1
        else:
            right = mid - 1

    return perfect_squares

# Example: Generate perfect squares between 1 and 50 using binary search
N = 50
result = generate_perfect_squares_binary(N)
print(f"Perfect squares between 1 and {N}: {result}")


# print(optimized(100))