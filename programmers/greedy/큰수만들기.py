def solution(number, k):
    max_number = find_max(number, k, 0)
    return str(max_number)
def find_max(number, k, n, result=0, visited=[]):
    if number in visited:
        return result
    visited += [number]
    if k==n:
        if result < int(number):
            return int(number)
        return result
    for i in range(len(number)):
        result = find_max(number[:i] + number[i+1:], k, n+1, result, visited)
    return result
    


print(solution("1924",	2)==	"94")
print(solution("1231234",	3)==	"3234")
print(solution("4177252841",	4)==	"775841")