from sys import stdin
while True:
    s=stdin.readline()[:-1]
    if not s: break
    counts=[0]*4
    for c in s:
        if c.islower():
            counts[0] += 1
        elif c.isupper():
            counts[1] += 1
        elif c.isnumeric():
            counts[2] += 1
        else:
            counts[3] += 1
    print(*counts)