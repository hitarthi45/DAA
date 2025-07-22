#factorial of n using recursion
def factorial(x):
    if x ==1:
        return 1
    elif x == 0:
        return 1
    else:
        return x*factorial(x-1)
print("Factorial is:", factorial(0))  # Call the function and print the result

#sum of n using recursion
def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)
print("Sum is:", sum(5))  # Call the function and print the result