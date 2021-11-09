def solution(priorities, location):
    n = len(priorities)
    waitlist = list(reversed(range(n)))
    printlist = []
    while waitlist:
        J = waitlist.pop()
        if len(waitlist) > 0 and priorities[J] < max(priorities):
            waitlist.insert(0, J)
        else:
            priorities[J] = 0
            printlist.append(J)
    return printlist.index(location) + 1
print(solution([2, 1, 3, 2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)