n=int(input())
d = [[0]*3 for _ in range(n)]

prices = []
for i in range(n):
    r,g,b = map(int, input().split())
    prices.append([r,g,b])
d[0][0] = prices[0][0]
d[0][1] = prices[0][1]
d[0][2] = prices[0][2]

for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + prices[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + prices[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + prices[i][2]

print(min(d[-1][0], d[-1][1], d[-1][2]))
