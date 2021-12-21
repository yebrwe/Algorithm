def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
n=int(input())
for i, c in enumerate(reversed(str(factorial(n)))):
    if c!='0':
        print(i)
        break