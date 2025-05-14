def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("Enter how many terms: "))
for i in range(n):
    print(fib_recursive(i), end=' ')
