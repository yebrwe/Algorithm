n=int(input())
for i in range(1, n+1):
    word=input()
    word=word.lower()
    wlen=len(word)
    for j in range(wlen//2):
        if word[j] != word[wlen-j-1]:
            print('#%d NO' %(i))
            break
    else:
        print('#%d YES' %(i))

