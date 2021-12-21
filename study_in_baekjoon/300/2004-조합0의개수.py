def fact_count(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count
n,m=map(int, input().split())

t = fact_count(n, 2) - fact_count(m, 2) - fact_count(n-m, 2)
f = fact_count(n, 5) - fact_count(m, 5) - fact_count(n-m, 5)
print(min(t,f))