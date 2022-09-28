n = int(input())
lst = list(map(int, input().split()))

sum_lst = [lst[0]]
for i in range(1,n):

    sum_lst.append(sum_lst[i-1]+lst[i])
ans = 0
for i in range(1, n-1):
    left = sum_lst[-1] - lst[i] - lst[0]
    right = sum_lst[-1] - sum_lst[i]
    ans = max(ans, left+right)

for i in range(1, n-1):
    left = sum_lst[i] - lst[0]
    right = sum_lst[-1] - lst[-1] - sum_lst[i-1]
    ans = max(ans, left + right)

for i in range(1, n-1):
    left = sum_lst[i-1]
    right = sum_lst[-1] - lst[-1] - lst[i]
    ans = max(ans, left+right)
print(ans)