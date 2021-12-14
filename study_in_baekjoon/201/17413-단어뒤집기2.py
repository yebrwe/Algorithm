def reverse_word(s):
    stack = []
    for c in s:
        stack.append(c)
    result = ''
    while stack:
        result += stack.pop()
    return result
s=input()
words=[]
word = ''
open = False
for c in s:    
    if c == '<':
        if word: words.append(word)
        word = c
        open = True
    elif c == '>':
        words.append(word + c)
        word = ''
        open = False
    else:
        word += c
words.append(word)

result = ''
for word in words:
    if '<' in word :
        result += word
    else:
        result += ' '.join([reverse_word(w) for w in word.split()])
print(result)
