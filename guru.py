def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
n = int(input("Enter the number of terms: "))
fibonacci_iterative(n)
