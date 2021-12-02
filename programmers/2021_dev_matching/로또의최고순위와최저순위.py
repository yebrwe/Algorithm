def solution(lottos, win_nums):
    checked = []
    max_count, min_count = 0, 0
    win_map = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    for lotto in lottos:
        if lotto in win_nums:
            checked += [lotto]
            max_count += 1
            min_count += 1
        else:
            if lotto == 0:
                max_count += 1
    return [win_map[max_count], win_map[min_count]]
print(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19])==	[3, 5])
print(solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25])==	[1, 6])
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35])==	[1, 1])