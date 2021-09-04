#unique_character_string


def unique1(s:str) -> bool:
  return len(set(s)) == len(s)

def unique2(s:str) -> bool:
  char = set()
  for letter in s:  
    if letter in char:
      return False
    else:
      char.add(letter)
  return True

print(unique1("aabbbccc")) #False
print(unique2("abc")) #True