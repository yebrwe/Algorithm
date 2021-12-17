s=input()
counts = [0]*26
for c in s:
    counts[ord(c) - ord('a')] += 1
print(*counts)
