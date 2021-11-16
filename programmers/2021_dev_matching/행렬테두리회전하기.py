def solution(rows, columns, queries):
    answer = []
    matrix = [[ columns*(i-1) + j for j in range(1, columns+1) ] for i in range(1, rows+1)]
    

    for x1,y1,x2,y2 in queries:
        tmp = matrix[x1-1][y1-1]
        minimum = tmp
        for x in range(x1-1, x2-1):
            matrix[x][y1-1] = matrix[x+1][y1-1]
            if minimum > matrix[x+1][y1-1]:
                minimum = matrix[x+1][y1-1]
        for y in range(y1-1, y2-1):
            matrix[x2-1][y] = matrix[x2-1][y+1]
            if minimum > matrix[x2-1][y+1]:
                minimum = matrix[x2-1][y+1]
        for x in range(x2-1, x1-1, -1):
            matrix[x][y2-1] = matrix[x-1][y2-1]
            if minimum > matrix[x-1][y2-1]:
                minimum = matrix[x-1][y2-1]
        for y in range(y2-1, y1-1, -1):
            matrix[x1-1][y] = matrix[x1-1][y-1]
            if minimum > matrix[x1-1][y-1]:
                minimum = matrix[x1-1][y-1]
        matrix[x1-1][y1] = tmp
        answer.append(minimum)
    return answer

print(solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]])==	[8, 10, 25])
print(solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])==	[1, 1, 5, 3])
print(solution(100,	97,	[[1,1,100,97]])==	[1])