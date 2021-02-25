def fibonacci(n):
    if n < 0:
        return "error"
    elif(n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

def factorial(num):

    factorial = 1
    if num < 0:
        factorial = str("error")
        return factorial
    elif num == 0:
        return factorial
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial

print(factorial(-1))