import re
def solution(files):
    answer = []
    for index, file in enumerate(files):
        it = re.findall('([a-zA-Z\.\- ]+)([0-9]+)(.*)',file)[0]
        answer.append([it[0].lower(), int(it[1]), index, file])
    return [a[3] for a in sorted(answer, key= lambda x: (x[0], x[1], x[2]))]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])