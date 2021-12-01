def solution(brown, yellow):
    answer = []
    sqrt_yellow = yellow**0.5
    #제곱
    if sqrt_yellow == int(sqrt_yellow):
      return [yellow+2, yellow+2]
    else:
      w = yellow+2
      h = 3
      #막대기
      if w*h == brown+yellow:
        answer = [w,h]
      #직사각형
      else:
        count = brown+yellow
        for i in range(count):
          w, h = i+1, int(count // (i+1))
          if w * h == count and (w-2) * (h-2) == yellow and w>h:
            answer = [w, h]
            break
    return answer
print(solution(10,	2))
print(solution(8,	1))
print(solution(24,	24))