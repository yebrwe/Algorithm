import sys
def to_bin(n):
  global res
  if n==0:
    return
  else:
    res=str(n%2) + res
    to_bin(n//2)

res=''
n=int(input())
to_bin(n)
print(res)
