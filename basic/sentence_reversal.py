#Sentence reversal
def reverse_words(str:str) -> str:  
  words=[]
  length = len(str)
  spaces = [' ']
  i=0

  while i<length:    
    if str[i] not in spaces:
      word_start = i
      while i<length and str[i] not in spaces:
        i+=1
      word_end = i
      word = str[word_start:word_end]
      words.append(word)
    else:
      i+=1
  return " ".join(my_reversed_using_stack(words))

from typing import List
def my_reversed(arr:List[str]) -> List[str]:
  new_arr = arr[:]
  length = len(arr)
  i=0
  while i<length:
    new_arr[i] = arr[length-i-1]
    i+=1
  return new_arr

def my_reversed_using_stack(arr:List[str]) -> List[str]:
  new_arr = []
  stack = []
  for s in arr:
    stack.append(s)
  while len(stack) > 0:
    new_arr.append(stack.pop())
  return new_arr

print(reverse_words("Hello World"))