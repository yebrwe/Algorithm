n=int(input())
words=set()
for _ in range(n):
    words.add(input())
for w in sorted(list(words), key=lambda x: (len(x), x)):
    print(w)