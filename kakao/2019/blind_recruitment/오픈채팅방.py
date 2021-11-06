def solution(record):
    answer = []
    last_name = {}
    history = []
    for r in record:
      rArr = r.split(' ')    
      if rArr[0] == 'Enter':
        last_name[rArr[1]] = rArr[2]
        history += [[rArr[0], rArr[1]]]
      elif rArr[0] == 'Leave':
        history += [[rArr[0], rArr[1]]]
      else:
        last_name[rArr[1]] = rArr[2]

      
    for [action, id] in history:
      if action == 'Enter':
        answer += [f'{last_name[id]}님이 들어왔습니다.']
      elif action == 'Leave':
        answer += [f'{last_name[id]}님이 나갔습니다.']
        

    return answer

print(solution(
  ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
) == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
)