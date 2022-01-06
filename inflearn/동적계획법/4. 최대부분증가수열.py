n=int(input())
arr=list(map(int, input().split()))
dp=[0]*(n+1)
dp[0]=1
for i in range(1, n):
    len=0
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[j]>len:
                len=dp[j]
    dp[i]=len+1
print(max(dp))