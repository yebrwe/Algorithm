def solution(info, query):
    answer = []
    hash = {}
    for row in info:
        [lang, job, grade, food, score] = row.split(" ")
        if '-' not in hash:
            hash['-'] = [int(score)]
        else:
            hash['-'].append(int(score))
        make(hash, [lang, job, grade, food], int(score))    
    for row in query:
        search = hash
        new_row = row.replace(" and ", " ").split(" ")
        for k in [k for k in new_row[:-1] if k != '-']:
            search = search[k]
        if 'value' in search:
            answer.append(len([v for v in search['value'] if v >= int(new_row[-1])]))
        else:
            answer.append(len([v for v in search['-'] if v >= int(new_row[-1])]))
            
    return answer

def make(hash, keys, score):
    if len(keys) == 0: return
    for i, key in enumerate(keys):
        if key not in hash:
            hash[key] = { 'value': [ score ] }
        else:
            hash[key]['value'].append(score)
        make(hash[key], keys[i+1:], score)

print(
    solution(
        ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
	    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    ) == [1,1,1,1,2,4]
)