import heapq as hq
def solution(jobs):
    answer = 0
    time = 0
    start = 0
    schedule = []
    finished = 0
    n = len(jobs)
    while finished < n:
        for r, t in jobs:
            if start <= r < time:
                hq.heappush(schedule, (t, r))
        if schedule:
            t, r = hq.heappop(schedule)
            finished += 1
            start = time
            time += t
            answer += time-r-1
        else:
            time += 1
    return answer // n