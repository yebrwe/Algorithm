N = int(input())
scores = list(map(int, input().split()))
avg = 0
max_score = max(scores)
print(sum([score / max_score * 100 for score in scores], 0) / N)