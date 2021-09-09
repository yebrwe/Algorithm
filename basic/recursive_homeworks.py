"""
problem1
0~n까지의  합  구하기
"""


"""
problem2
1234 각 자리 숫자 더하기
"""

"""
problem3
문자열을 문자 리스트로 스플릿하기
"""


def solve1(n:int) -> int:
    if n == 0:
        return 0
    else:
        return n + solve1(n-1)
print(solve1(4))


from abc import abstractmethod
import math
def solve2(n:int) -> int:
    if n == 0:
        return 0
    else:
        return n%10 + solve2(math.floor(n/10))
print(solve2(123456))

from typing import List
def solve3(str:str, words:List[str], result=None)->List[str]:
    
    if not result:
        result:List[str] = []
    for word in words:
        if str.startswith(word):
            result.append(word)
            return solve3(str[len(word):], words, result)
    return result

print(solve3('themanran', ['the', 'man', 'ran']))

