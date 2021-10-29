# python 기본 배열로 큐를 사용하면 매우 느리므로 deque 라이브러리를 사용할 것
from collections import deque

# 이진검색 라이브러리
import bisect

# 시계 방향으로 90도 회전
def rotate90(arr):
    n = len(arr)
    tmp = [ [0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-1-j][i]
    return tmp

# N x N 배열 전체 왼쪽으로 1칸 이동
def shift_array_to_left(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if j+1 > n-1: continue
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

# N x N 배열 전체 위로 1칸 이동
def shift_array_to_top(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i+1 > n-1: continue
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
