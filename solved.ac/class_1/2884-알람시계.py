hh, mm = map(int, input().split())
ss = hh*3600 + mm*60 - 45*60
print((ss//3600+24)%24, ss%3600//60)