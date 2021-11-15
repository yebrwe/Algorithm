def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return get_hhmmdd(0)
    n = get_second(play_time)
    timelines = [0] * (n+1)
    for log in logs:
        for f, t in [map(get_second, log.split('-'))]:
            timelines[f] += 1
            timelines[t] -= 1
    
    for i in range(1, n):
        timelines[i] = timelines[i] + timelines[i-1]

    max_time = 0
    max_left = 0
    adv_sum = 0

    
    left = 0
    right = get_second(adv_time)
    for i in range(left, right):
        adv_sum += timelines[i]

    while right <= n:        
        if max_time < adv_sum:
            max_time = adv_sum
            max_left = left
        adv_sum -= timelines[left]
        if right < n:
             adv_sum += timelines[right]
        left += 1
        right += 1
        
    return get_hhmmdd(max_left)

def get_second(time):
    hh, mm, ss = map(int, time.split(':'))
    return hh*3600 + mm*60 + ss

def get_hhmmdd(time):
    hh = time // 3600
    hh = f'0{hh}' if hh < 10 else f'{hh}'
    mm = time % 3600 // 60
    mm = f'0{mm}' if mm < 10 else f'{mm}'
    ss = time % 3600 % 60
    ss = f'0{ss}' if ss < 10 else f'{ss}'
    return ':'.join([ hh, mm, ss ])
    

print(solution("02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]) == "01:30:59")
print(solution("99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]) == 	"01:00:00")
print(solution("50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]) == 	"00:00:00")


