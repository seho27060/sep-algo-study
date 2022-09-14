N = int(input())
arr = []
for _ in range(N):
    ar = list(input().split())
    arr += ar
sorted_arr = sorted(arr, key=lambda x:(x[0], int(x[2:])), reverse=True)

q = []
while arr:
    x = arr.pop(0)
    while x:
        if x == sorted_arr[-1]:
            sorted_arr.pop()
            x = 0
        elif q and q[-1] == sorted_arr[-1]:
            q.pop()
            sorted_arr.pop()
        else:
            q.append(x)
            x = 0

while sorted_arr:
    if q[-1] == sorted_arr[-1]:
        q.pop()
        sorted_arr.pop()
    else:
        break

if not q:
    print('GOOD')
else:
    print('BAD')