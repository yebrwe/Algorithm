def solution(brown, yellow):
    count = brown+yellow
    sqrt_yellow = yellow**0.5
    #제곱
    if sqrt_yellow == int(sqrt_yellow):
      return [sqrt_yellow+2, sqrt_yellow+2]
    #그외
    for i in range(count):
      w, h = i+1, int(count // (i+1))
      if w * h == count and (w-2) * (h-2) == yellow and w>h:
        return[w, h]
    return []
print(solution(10,	2))
print(solution(8,	1))
print(solution(24,	24))
print(solution(12,	4))