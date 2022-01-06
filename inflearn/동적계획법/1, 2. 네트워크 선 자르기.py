n=int(input())
# Bottom-Up
# a=[0]*101
# a[1]=1
# a[2]=2
# for i in range(3, n+1):
#     a[i]=a[i-1]+a[i-2]
# print(a[n])
# Top-Down
memo=[0]*101
def f(n):
    if n==1 or n==2:
        return n
    elif memo[n]!=0:
        return memo[n]
    memo[n]=f(n-1) + f(n-2)
    return memo[n]
print(f(n))