
from itertools import combinations
def solution(distance, rocks, n):
    removes = []
    removes.extend(combinations(rocks, n))
    print(removes)

    removed_rocks = set()
    for remove in removes:
        removed_rocks.add(tuple([rock for rock in rocks if rock not in remove]))

    
    print(removed_rocks)
    answer = 0
    return answer

print(solution(25,	[2, 14, 11, 21, 17],	2)	==4)