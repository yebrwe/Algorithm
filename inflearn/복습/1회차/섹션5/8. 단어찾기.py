n=int(input())
ch=dict()
for _ in range(n):
  word=input()
  ch[word]=0
for _ in range(n-1):
  word=input()
  ch[word]+=ch.get(word, 0) + 1
for k in ch:
  if ch[k]==0:
    print(k)