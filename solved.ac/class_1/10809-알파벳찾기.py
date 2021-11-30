word = input()
alpha = [chr(ord('a')+i) for i in range(26)]
count = {}
for c in alpha:
    if c not in count: count[c]=-1
    if c in list(word):
        count[c] = list(word).index(c)
print(' '.join([str(cnt) for cnt in count.values()]))