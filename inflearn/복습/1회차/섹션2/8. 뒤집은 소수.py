def reverse(x):
    res=0    
    while x>0:
        res=res*10 + x%10
        x=x//10
    return res
def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True
n=int(input())
a=list(map(int, input().split()))
for x in a:
    tmp=reverse(x)
    if tmp==2 or tmp==3:
        print(tmp, end=' ')
    elif tmp > 1 and isPrime(tmp):
        print(tmp, end=' ')

