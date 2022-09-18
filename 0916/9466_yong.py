# dfs 문제
# 학생들의 정보를 순서대로 탐색하며 싸이클을 판단
# 싸이클의 정보를 활용해 최대한 탐색을 줄여가며 팀을 이루지 못한 학생들을 찾는다.

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def dfs(val):
    lst = deque([val])
    check[val] = val
    q = deque()
    q.append(arr[val]-1)
    while q:
        target = q.popleft()
        if target == val:
            return
        if check[target] == -1:
            if target < val:
                for i in lst:
                    check[i] = -2
                return
            else:
                check[target] = val
                lst.append(target)
                q.append(arr[target]-1)
        else:
            if check[target] != val:
                for i in lst:
                    check[i] = -2
                return
            else:
                idx = lst.index(target)
                for i in range(idx):
                    check[lst[i]] = -2
                return


for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    check = [-1] * n
    for i in range(n):
        if check[i] == -1:
            if i == arr[i]-1:
                check[i] = i
            else:
                dfs(i)
    # print(check)
    print(check.count(-2))