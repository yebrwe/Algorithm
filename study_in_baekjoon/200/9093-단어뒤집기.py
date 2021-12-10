def reverse(word):
    str = ''
    while word:
        str += word.pop()
    return str
n=int(input())
for _ in range(n):
    print(' '.join([reverse(list(w)) for w in input().split()]))
