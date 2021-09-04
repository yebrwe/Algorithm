#Annagram



def annagram1(s1:str, s2:str)->bool:
  s1 = s1.replace(' ', '').lower()
  s2 = s2.replace(' ', '').lower()
  return sorted(s1) == sorted(s2)

def annagram2(s1:str, s2:str)->bool:
  s1 = s1.replace(' ', '').lower()
  s2 = s2.replace(' ', '').lower()

  if len(s1) != len(s2):
    return False
  
  count = {}
  for letter in s1:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1

  for letter in s2:
    if letter in count:
      count[letter] -= 1
    else:
      count[letter] = 1
  
  for k in count:
    if count[k] != 0: return False
  
  return True

print(annagram1("dog", "god")) #True
print(annagram1("dag", "god")) #False
print(annagram2("dog", "god")) #True
print(annagram2("dag", "god")) #False