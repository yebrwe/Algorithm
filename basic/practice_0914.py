from typing import List
#fibonnaci
def fibonnaci(n:int):
    a=0
    b=1
    for _ in range(n):
        a, b = b, a+b
    return a
print(fibonnaci(7))
    

#permutation
def permutation(str:str)->List[str]:
    output = []
    
    if len(str) == 1:
        return [str]
    for i, s in enumerate(str):
        for c in permutation(str[i+1:]+str[:i]):
            output += [s+c]
    return output
print(permutation('abc'))
print(permutation('dog'))


#minimum change coin
memz = [0] * 100
def change_coin(n:int, coins:List[int])->int:
    min = n
    if n in coins:
        return 1
    if memz[n] > 0:
        return memz[n]
    for coin in coins:
        for i in [c for c in coins if c <= n]:
            cv =  1 + change_coin(n-i, coins)
            if min > cv:
                min = cv
                memz[n] = min
    return min
print(change_coin(75, [1,3,5,11,15]))