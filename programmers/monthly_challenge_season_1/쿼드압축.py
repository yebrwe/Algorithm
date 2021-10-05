def solution(arr):
    answer = [0, 0]
    for i in compress(arr):
        answer[i] += 1
    return answer

def compress(arr): 
    n = len(arr)
    if n == 1:
        return [arr[0][0]]
    elif len(set(sum(arr, []))) == 1:
        return [arr[0][0]]
    topleft = [ [ arr[i][j] for j in range(n//2)] for i in range(n//2)]
    topright = [ [ arr[i][j] for j in range(n//2, n)] for i in range(n//2)]
    bottomleft = [ [ arr[i][j] for j in range(n//2)] for i in range(n//2, n)]
    bottomright = [ [ arr[i][j] for j in range(n//2, n)] for i in range(n//2, n)]
    return compress(topleft) + compress(topright) + compress(bottomleft) + compress(bottomright)

print(solution(
    [[1,1,0,0]
    ,[1,0,0,0]
    ,[1,0,0,1]
    ,[1,1,1,1]]
))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))