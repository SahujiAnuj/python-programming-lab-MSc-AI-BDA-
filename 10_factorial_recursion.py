# 10_factorial_recursion.py

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter number: "))
print("Factorial:", factorial(num))
