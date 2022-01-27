def check():
    ch=[0]*10
    for i in range(9):
        for j in range(9):        
            ch[board[i][j]]+=1
            ch[board[j][i]]-=1
    if sum(ch)!=0:
        return False

    for i in range(3):
        for j in range(3):
            ch=[0]*10
            for k in range(3):
                for l in range(3):
                    ch[board[3*i+k][3*j+l]]=1
            if sum(ch)!=9:
                return False
    return True
board=[list(map(int, input().split())) for _ in range(9)]
if check():
    print('YES')
else:
    print('NO')


    