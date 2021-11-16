def solution(rows, columns, queries):
    answer = []
    matrix = [[ columns*(i-1) + j for j in range(1, columns+1) ] for i in range(1, rows+1)]
    

    for t,l,b,r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1
        tmp = matrix[top][left]
        minimum = tmp
        for r in range(top, bottom):
            matrix[r][left] = matrix[r+1][left]
            if minimum > matrix[r+1][left]:
                minimum = matrix[r+1][left]
        for c in range(left, right):
            matrix[bottom][c] = matrix[bottom][c+1]
            if minimum > matrix[bottom][c+1]:
                minimum = matrix[bottom][c+1]
        for r in range(bottom, top, -1):
            matrix[r][right] = matrix[r-1][right]
            if minimum > matrix[r-1][right]:
                minimum = matrix[r-1][right]
        for c in range(right, left, -1):
            matrix[top][c] = matrix[top][c-1]
            if minimum > matrix[top][c-1]:
                minimum = matrix[top][c-1]
        matrix[top][left+1] = tmp
        answer.append(minimum)
    return answer

print(solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]])==	[8, 10, 25])
print(solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])==	[1, 1, 5, 3])
print(solution(100,	97,	[[1,1,100,97]])==	[1])