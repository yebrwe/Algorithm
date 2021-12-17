s=input()
arr=[]
pos=[-1]*26
for i, c in enumerate(s):
    if c not in arr:
        arr.append(c)
        pos[ord(c)-ord('a')] = i
print(*pos)