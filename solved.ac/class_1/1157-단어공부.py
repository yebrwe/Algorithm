word = input().lower()
hash={}
for c in word:
    if c not in hash:
        hash[c] = 0
    hash[c]+=1
cnt = 0
max = -1
rst = ''
for k in hash:
    if max <= hash[k]: 
        max = hash[k]        
        rst = k
for k in hash:
    if max == hash[k]: cnt += 1
if cnt == 1: print(rst.upper())
else: print('?')