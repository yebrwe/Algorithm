#coin change

from typing import List
from nose.tools import assert_equal
n= 100
known_result = [0] * (n+1)
class TestCase:
    def test(self, solution):
        coins = [1,5,10,25]
        assert_equal(solution(45, coins), 3)
        assert_equal(solution(23, coins), 5)
        assert_equal(solution(74, coins), 8)
        print('PASSED ALL PROBLEM.')

    def test2(self, solution):
        coins = [1,5,10,25]
        assert_equal(solution(45, coins, known_result), 3)
        assert_equal(solution(23, coins, known_result), 5)
        assert_equal(solution(74, coins, known_result), 8)
        print('PASSED ALL PROBLEM.')
def rec_coin(n:int, coins:List[int]):
    min = n
    
    if n in coins:
        return 1
    else:
        for coin in coins:
            new_coins = []
            for c in coins:
                if n >= c:
                    new_coins.append(c)
            for i in new_coins:
                cnt = 1 + rec_coin(n-i, coins)
                if min > cnt:
                    min = cnt
            return min


def rec_coin_dynamic(n:int, coins:List[int], known_result):
    min = n
    if n in coins:
        return 1
    elif known_result[n] > 0:
        return known_result[n]
    else:
        for coin in coins:
            new_coins = []
            for c in coins:
                if n >= c:
                    new_coins.append(c)
            for i in new_coins:
                cnt = 1 + rec_coin_dynamic(n-i, coins, known_result)
                if min > cnt:
                    min = cnt
                    known_result[n] = min
            return min
    



t = TestCase()
# t.test(rec_coin)
t.test2(rec_coin_dynamic)