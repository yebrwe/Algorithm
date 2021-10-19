def solution(dartResult):
    oper = {'S': 1, 'D': 2, 'T': 3}
    score = ''
    rounds = []    
    for c in dartResult:
        if c in oper:
            rounds.append(int(score) ** oper[c])
            score = ''
        elif c == '*':
            rounds[-1] *= 2
            if len(rounds) > 1:
                rounds[-2] *= 2
        elif c == '#':
            rounds[-1] *= -1            
        else:
            score += c
    return sum(rounds, 0)


# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))