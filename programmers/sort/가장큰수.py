def solution(numbers):
    return str(int(''.join([str(n) for n in sorted(numbers, key=comp, reverse=True)])))
def comp(x): 
    if 0<=x<10:
        return str(x)*4
    elif 10<=x<100:
        return str(x)*2
    elif 100<=x<1000:
        return (str(x)*2)[:4]
    return str(x)

print(solution([6, 10, 2]) ==	"6210")
print(solution([3, 30, 34, 5, 9]) ==	"9534330")
print(solution([121,12]) ==	"12121")
# print(solution([6, 10, 2]))
# print(solution([900,901,910]))