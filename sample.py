# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input number
num = int(input("Enter a number: "))

# Call the factorial function and print the result
result = factorial(num)
print(f"The factorial of {num} is: {result}")
