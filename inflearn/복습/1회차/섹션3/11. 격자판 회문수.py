board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(7):
    for j in range(3):
        tmp = board[i][j:j+5]
        if tmp == tmp[::-1]:
            cnt+=1

for i in range(3):
    for j in range(7):
        for k in range(3):
            if board[i+k][j] != board[4+i-k][j]:
                break
        else:
            cnt+=1
print(cnt)