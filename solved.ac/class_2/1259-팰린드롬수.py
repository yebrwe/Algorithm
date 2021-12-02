while True:
    w=input()
    if w=='0':break
    if w==w[::-1]:
        print('yes')
    else:
        print('no')