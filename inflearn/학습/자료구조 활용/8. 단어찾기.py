n=int(input())
hash=dict()
for _ in range(n):
    word = input()
    hash[word]=0

for _ in range(n-1):
    word = input()
    hash[word]=1

for k in hash:
    if hash[k] == 0:
        print(k)