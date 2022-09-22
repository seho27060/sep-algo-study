import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0

for i in range(N):
    # 타겟 숫자를 제외한 나머지 리스트
    arr = lst[:i]+lst[i+1:]
    left = 0
    right = len(arr)-1
    while left<right:
        x = arr[left]+arr[right]
        if x==lst[i]:
            ans+=1
            break
        if x<lst[i]:
            left+=1
        else:
            right-=1
print(ans)