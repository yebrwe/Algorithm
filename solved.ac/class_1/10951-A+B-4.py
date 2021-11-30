import sys
lines = sys.stdin.readlines()
for s in lines:
    a,b = map(int, s.split())
    print(a+b)
