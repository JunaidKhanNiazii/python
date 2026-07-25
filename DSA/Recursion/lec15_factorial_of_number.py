# n = int(input("Enter your number:"))
# fact = 1
# def factorial(n, fact):
#     if n == 0 or n == 1:
#         return fact
#     else:
#         fact = fact * n
#         n -= 1
#         print(n, fact)
#         return factorial( n,fact)

# print(factorial(n, fact))

# method 2

n = int(input("Enter your number:"))

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return (n * factorial(n-1))

print(factorial(n))