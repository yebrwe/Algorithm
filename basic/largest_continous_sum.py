#[1,2,-1,3,4,10,10,-10,-1]
# Largest continous sum
from typing import List
def largest_contious_sum(arr:List[int])->int:
  if len(arr)==0:
    return 0
  current_sum=0
  max_sum=0

  for num in arr:
    current_sum = max(current_sum+num, num)
    max_sum = max(current_sum, max_sum)
  return max_sum

print(largest_contious_sum([1,2,-4,3,4,10,10,-10,-1]))