n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

lst_sum = set()
for x in lst:
    for y in lst:
        lst_sum.add(x+y)
lst.sort()
ans = 0
flag = 0
def find():
    global ans
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            if lst[i] - lst[j] in lst_sum:
                ans = lst[i]
                return
find()
print(ans)
