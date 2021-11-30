count = -1
numbers = []
for _ in range(9):
    numbers.append(int(input()))
max_number = max(numbers)
for i in range(len(numbers)):
    if max_number == numbers[i]:
        count = i+1
print(max_number)
print(count)