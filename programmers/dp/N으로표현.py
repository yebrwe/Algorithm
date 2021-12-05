def solution(N, number):
    dp=[[]]
    for i in range(1, 9):
      temp = []
      for j in range(1, i):
        for k in dp[j]:
          for l in dp[i-j]:
            if l==0:continue
            temp.append(k+l)
            temp.append(k-l)
            temp.append(k*l)
            temp.append(k//l)
      temp.append(int(N*int('1'*i)))
      dp.append(list(set(temp)))
      if number in temp:
        return i
    return -1
print(solution(5,	12)==	4)
print(solution(2,	11)==	3)