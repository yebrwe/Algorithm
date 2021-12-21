T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = numbers[s-1:e]
    numbers.sort()
    print('#%d %d' %(t+1, numbers[k-1]))