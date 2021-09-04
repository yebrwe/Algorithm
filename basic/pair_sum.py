#Pair Sum
def pair_sum(arr:list, k:int)->int:
  seen = set()
  output = set()

  for num in arr:
    target = k-num
    if target not in seen:
      seen.add(num)
    else:
      output.add((min(target, num), max(target, num)))
      print((min(target, num), max(target, num)))
  
  return len(output)

print(pair_sum([1,2,2,3], 4))