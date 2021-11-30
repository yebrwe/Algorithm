n=int(input())
A = [0] * 1001
A[1] = 1
A[2] = 2
for i in range(3, n+1):
    A[i] = (A[i-1] + A[i-2]) % 10007
print(A[n])