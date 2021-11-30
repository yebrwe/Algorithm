n, x = map(int, input().split())
numbers = list(map(int, input().split()))
print(' '.join([str(number) for number in numbers if number < x]))