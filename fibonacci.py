def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input for the number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Display the Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = [fibonacci(i) for i in range(1, num_terms + 1)]
    print(f"Fibonacci series up to {num_terms} terms:", fib_series)
