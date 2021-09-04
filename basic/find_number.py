#find number
from typing import List
import collections
def finder1(arr1:List[int], arr2:List[int]) -> int:
  arr1.sort()
  arr2.sort()
  for num1, num2 in zip(arr1,arr2):
    if num1 != num2:
      return num1
  return arr1[-1]

def finder2(arr1:List[int], arr2:List[int]) -> int:
  d = collections.defaultdict(int)

  for num in arr2:
    d[num] += 1
  
  for num in arr1:
    if d[num] == 0:
      return num
    else:
      d[num] -= 1

print(finder2([1,2,2,2,5,6,7,3], [2,2,2,1,5,6,7]))