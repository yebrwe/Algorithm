#수험번호, 문제번호, 점수
def solution(logs):
    answer = []
    hash = {}
    for log in logs:        
        [test_num, problem_num, score] = log.split(' ')
        score = int(score)        
        if test_num not in hash:
            hash[test_num] = {}
        if problem_num not in hash[test_num]:
            hash[test_num][problem_num] = score
        if hash[test_num][problem_num] < score:
            hash[test_num][problem_num] = score
    
    
    for index, l1 in enumerate(logs): 
        l1_arr = l1.split(' ')
        for l2 in logs[:index] + logs[index+1:]:
            l2_arr = l2.split(' ')
            if sorted(hash[l1_arr[0]].keys()) == sorted(hash[l2_arr[0]].keys()) and hash[l1_arr[0]].keys() > 4:
                flag = True
                for k in hash[l1_arr[0]]:
                    if hash[l2_arr[0]][k] != hash[l2_arr[0]][k]:
                        flag = False
                
                if flag and l1_arr[0] not in answer:                    
                    answer.append(l1_arr[0])
    return sorted(answer) if len(answer) > 0 else ["None"]
# solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])
# solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"])
solution(["1901 10 50", "1909 10 50"])
