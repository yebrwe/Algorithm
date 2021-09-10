#reverse a string
from nose.tools import assert_equal

class TestCase():

    def test(self, solution):
        assert_equal(solution("hello"), "olleh")
        assert_equal(solution("hello world"), "dlrow olleh")
        assert_equal(solution("123456789"), "987654321")
        print("TEST CASE ALL PASS!!")

def reverse(str:str)->str:
    n = len(str)
    if n == 1:
        return str
    return str[n-1] + reverse(str[:n-1])

tc = TestCase()
tc.test(reverse)