def solution(progresses, speeds):
    answer = []
    
    q = []
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) // speed + (1 if (100 - progress) % speed > 0 else 0)
        q.insert(0, day)
    
    cnt = 1
    day = 0
    while q:
        day = q.pop()
        # print(day, cnt)
        for _ in range(len(q)):       
            if day >= q[-1]:            
                cnt += 1
                q.pop()
            else:
                answer.append(cnt)
                cnt = 1
                break
    answer.append(cnt)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))