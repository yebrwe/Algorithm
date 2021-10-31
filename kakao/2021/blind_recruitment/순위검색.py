import bisect
def solution(info, query):
    answer = []
    hash = make_hash()
    for row in info:
        [lang, job, grade, food, score] = row.split(" ")
        score = int(score)
        for a in [lang, '-']:
            for b in [job, '-']:
                for c in [grade, '-']:
                    for d in [food, '-']:
                        hash[a+b+c+d].append(score)

    for a in hash.values():
        a.sort()

    for q in query:
        [a, b, c, d, score] = q.replace(' and ', ' ').split(' ')
        score = int(score)
        arr = hash[a+b+c+d]
        answer.append(len(arr) - bisect.bisect_left(arr, score))
    return answer

def make_hash():
    hash = {}
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    hash[a+b+c+d] = []
    return hash
print(
    solution(
        ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
	    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    ) == [1,1,1,1,2,4]
)