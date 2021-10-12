def solution(genres, plays):
    answer = []    
    #장르>>재생>>고유번호
    album = {}
    sum = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in sum:
            album[g] = [[p, i]]
            sum[g] = p
        else:
            album[g].append([p, i])
            sum[g] += p
    
    first = [0, '']
    second = [0, '']
    for key in sum:
        if sum[key] > first[0]:
            first[0] = sum[key]
            first[1] = key
    
    for key in sum:
        if key == first[1]: continue
        if sum[key] > second[0]:
            second[0] = sum[key]
            second[1] = key

    for key in [first[1], second[1]]:
        l = len(album[key])
        for i in range(l):
            for j in range(i+1, l):
                if album[key][i][0] < album[key][j][0]:
                    album[key][i], album[key][j] = album[key][j], album[key][i]
                elif album[key][i][0] == album[key][j][0] and album[key][i][1] < album[key][j][1]:
                    album[key][i], album[key][j] = album[key][j], album[key][i]

        for i in range(2 if l > 2 else l):
            answer += [album[key][i][1]]
    
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))