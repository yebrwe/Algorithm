def solution(m, n, puddles):
  roads = [[0]*m for _ in range(n)]
  roads[0][0]= 1
  for i in range(n):
    for j in range(m):
      if i==0 and j==0:continue
      if [j+1,i+1] in puddles: continue
      roads[i][j] = roads[i-1][j] + roads[i][j-1]
  return roads[n-1][m-1] % 1000000007
print(solution(4,	3,	[[2, 2]]) ==	4)

