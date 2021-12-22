from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        a = people.pop()
        if people and a + people[0] <= limit:
            people.popleft()
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100)==	3)
print(solution([70, 80, 50], 100)==	3)
print(solution([16, 15, 14, 6, 5, 4], 20)==	3)