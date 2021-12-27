n,m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
left=0
right=n-1
while left<=right:
    mid = (left + right) //2
    if a[mid] < m:
        left = mid + 1
    elif a[mid] > m:
        right = mid - 1
    else:
        break
print(mid+1)