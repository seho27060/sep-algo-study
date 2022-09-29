# 백준 21758 꿀 따기 - 누적합

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0
sumarr = []
sumarr.append(arr[0])

for i in range(1, N):
    sumarr.append(sumarr[i-1] + arr[i]) # 누적 합 배열 만들기

# print(sumarr)

# 꿀-벌-벌  -> 꿀통이 제일 왼쪽, 벌 맨 오른쪽 고정, 남은 한마리 위치만 고르면 됨 -> 벌이 있으면 꿀 채취를 못함!!
for i in range(1, N-1):
    # 맨마지막칸 꿀 채취불가 -> sumarr[N-2]
    # arr[i] -> 벌 위치는 채집 불가 -> for문을 돌면서 한 자리씩 넣어보기
    ans = max(ans, sumarr[N-2] + sumarr[i-1] - arr[i])

# 벌-벌-꿀
for i in range(1, N-1):
    ans = max(ans, sumarr[N-1] - arr[0] - arr[i] + sumarr[N-1] - sumarr[i] )

# 벌-꿀-벌   => 이 상황은 당연스레 벌은 좌 우 끝, 꿀통 자리만 찾으면 된다
for i in range(1, N-1):
    ans = max(ans, sumarr[N-2] - arr[0] + arr[i])

print(ans)
