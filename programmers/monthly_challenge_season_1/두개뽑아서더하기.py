def solution(numbers):
    output = set()
    for i, n in enumerate(numbers):
        for nn in (numbers[:i] + numbers[i+1:]):
            output.add(n+nn)
    return sorted(list(output))
