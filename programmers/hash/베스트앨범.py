#장르 오름차순
#재생 오름차순
#고유번호 내림차순
def solution(genres, plays):
    answer = []
    album = {}
    sum = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in sum:
            album[g] = [[p, i]]
            sum[g] = p
        else:
            album[g].append([p, i])
            sum[g] += p

    for k in sorted(sum, key=lambda x: -sum[x]):
        answer += [i for _, i in sorted(album[k], key = lambda x: -x[0])[:2]]
    return answer



print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic"], [300]))