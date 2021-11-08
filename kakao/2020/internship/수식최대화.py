import re
from itertools import permutations
def solution(expression):
    answer = 0
    ops = set(re.findall('[^0-9]', expression))
    for ops in list(permutations(ops, len(ops))):
        for op in ops:
            arr = re.findall('[0-9]+\\' + op + '[0-9]+', expression)
            print(arr)
            # if op == '-':

            # elif op == '+':

            # elif op == '*':
            
    return answer
print(solution("100-200*300-500+20")== 	60420)
# print(solution("-100-200-100-200+20")== 	60420)