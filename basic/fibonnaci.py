
# fibonnaci

from nose.tools import assert_equal
import time
n=100
cache = [None] * (n+1)


class TestCase():
    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)        
        print('ALL PASS!')
def feb_iter(n:int) -> int:
    if n == 1 or n == 2:
        return 1
    pp = 1
    p = 1
    c = 0
    for _ in range(n-2):
        c = p + pp
        pp = p
        p = c
    return c
def feb_rec(n:int) -> int:
    if n == 1 or n == 2:
        return 1
    return feb_rec(n-2) + feb_rec(n-1)

def feb_dyn(n:int) -> int:
    if n == 1 or n == 2:
        return 1
    if cache[n]:
        return cache[n]
    cache[n] = feb_dyn(n-2) + feb_dyn(n-1)
    return cache[n]

t = TestCase()

start = time.time()
t.test(feb_iter)
print("feb_iter time :", time.time() - start)  # 속도 순위 2 (반복문)
start = time.time()
t.test(feb_rec)
print("feb_rec time :", time.time() - start)  # 속도 순위 3 (재귀)
start = time.time()
t.test(feb_dyn)
print("feb_dyn time :", time.time() - start)  # 속도 순위 1 (재귀+메모이제이션)

