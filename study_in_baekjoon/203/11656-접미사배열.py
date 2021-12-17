s=input()
prefixes = []
for i in range(len(s)):
    prefixes.append(s[i:])
print('\n'.join([prefix for prefix in sorted(prefixes)]))