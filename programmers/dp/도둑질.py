def solution(money):
    n = len(money)
    
    dp = [0] * n
    dp[0]=money[0]
    dp[1]=dp[0]
    for i in range(2, n):
        dp[i] = max([dp[i-1], dp[i-2] + money[i]])

    dp2 = [0] * n
    dp2[0]=0
    dp2[1]=money[1]    
    for i in range(2, n):
        dp2[i] = max([dp2[i-1], dp2[i-2] + money[i]])
    return max([dp[-2], dp2[-1]])

print(solution([1, 2, 3, 1])==	4)