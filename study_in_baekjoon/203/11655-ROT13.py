s=input()
result = ''
for c in s:
    if c.isupper():
        result += chr(ord('A') + (ord(c) - ord('A') + 13) % 26)
    elif c.islower():
        result += chr(ord('a') + (ord(c) - ord('a') + 13) % 26)
    else:
        result += c
print(result)