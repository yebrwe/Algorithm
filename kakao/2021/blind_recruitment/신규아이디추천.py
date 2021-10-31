import re
def solution(new_id):
    answer = ''
    answer = re.sub("[^0-9a-zA-Z_\.\-]", "", new_id.lower())
    answer = re.sub("\.{1,}", ".", answer)

    while answer.startswith("."):
        answer = answer[1:]
    while answer.endswith("."):
        answer = answer[:-1]

    if not answer:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        while answer.endswith("."):
            answer = answer[:-1]
    if len(answer) <=2:
        last_word = answer[-1]
        while len(answer) < 3:
            answer += last_word
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm") == 	"bat.y.abcdefghi")
print(solution("z-+.^.") == 	"z--")
print(solution("=.=") == 	"aaa")
print(solution("123_.def") == 	"123_.def")
print(solution("abcdefghijklmn.p") == 	"abcdefghijklmn")