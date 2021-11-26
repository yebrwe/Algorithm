from itertools import permutations
def solution(numbers):
    primes = set()
    for i in range(1, len(numbers) + 1):
        for number in set(permutations(numbers, i)):
            prime = int(''.join(number))
            if prime <= 1:continue
            flag = False
            for i in range(2, prime-1):
                if prime % i == 0:
                    flag = True
                    break
            if not flag:
                primes.add(prime)
    return len(primes)

print(solution("17")==	3)
print(solution("011")==	2)