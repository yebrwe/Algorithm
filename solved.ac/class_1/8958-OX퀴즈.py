T=int(input())
for _ in range(T):
    quiz = input()
    while 'XX' in quiz:
        quiz=quiz.replace('XX', 'X')
    scores = quiz.split('X')
    score_sum = 0
    for score in scores:
        score_sum += sum([i+1 for i in range(len(score))], 0)
    print(score_sum)