def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(numbers)):
      s=s.replace(numbers[i], str(i))
    return int(s)
print(solution("one4seveneight")==	1478)
print(solution("23four5six7")==	234567)
print(solution("2three45sixseven")==	234567)
print(solution("123")==	123)