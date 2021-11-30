T=int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ''.join([c*R for c in S])
    print(P)
