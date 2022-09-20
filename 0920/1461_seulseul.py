import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

L = []
R = []
for book in books:
    if book < 0:
        L.append(abs(book))
    else:
        R.append(book)

cost = []

def func(arr):
    arr.sort()
    cnt=0
    while arr:
        x=arr.pop()
        if not cnt:
            cost.append(x)
        cnt+=1
        if cnt==M:
            cnt=0
func(L)
func(R)

cost.sort()
print(cost)
print(cost[-1]+sum(cost[:-1])*2)