n = int(input())
k = int(input())

lst = list(map(int, input().split()))
if k >= n:
    print(0)
else:
    lst.sort()
    ans = []
    for i in range(1, n):
        ans.append(lst[i] - lst[i-1])
    ans.sort()
    for _ in range(k-1):
        ans.pop()

    print(sum(ans))