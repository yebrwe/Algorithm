#'abc' => ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#'dog' => ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']
from typing import List
from nose.tools import assert_equal

class TestCase():
    def test(self, solution):
        assert_equal(sorted(solution("abc")), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution("dog")), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])    )
        print("TEST CASE ALL PASS!!")

def permute(s:str)->List[str]:
    output = []
    if len(s) == 1:
        return [s]
    for i, letter in enumerate(s):
        print('letter is :' + letter)
        for perm in permute(s[i+1:]+s[:i]): 
            
            output += [letter + perm]
            print(output)
    
    return output
tc = TestCase()
tc.test(permute)
