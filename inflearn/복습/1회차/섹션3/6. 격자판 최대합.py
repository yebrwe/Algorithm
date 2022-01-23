n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]

res=0
for i in range(n):
    sum1=0
    sum2=0
    for j in range(n):
        sum1+=board[i][j]
        sum2+=board[j][i]
    if sum1>res:
        res=sum1
    if sum2>res:
        res=sum2
sum3=0
sum4=0
for i in range(n):    
    sum3+=board[i][i]
    sum4+=board[i][n-i-1]
if sum3>res:
    res=sum3
if sum4>res:
    res=sum4
print(res)