N = int(input())
arr = set()
ans = 0
for i in range(N):
    arr.add(int(input()))

sum = set()
for i in arr:
    for j in arr:
        sum.add(i+j)

for i in arr:
    for j in arr:
        if i-j in sum:
            ans = max(ans, i)

print(ans)