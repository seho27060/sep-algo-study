# 투포인터 문제
# 한 원소를 제외한 리스트에서 투포인터를 활용해 두 원소의 합이 선택한 원소의 합과 같은지 판단

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in range(N):
    lst = arr[:i] + arr[i+1:]
    l = 0
    r = len(lst) -1
    while l < r:
        val = lst[l] + lst[r]
        if val == arr[i]:
            ans += 1
            break
        if val < arr[i]:
            l += 1
        else:
            r -= 1
print(ans)