def check(X):
    ST = [X[0]]
    visit = [0]*(N+1)
    visit[X[0]] = 1
    c = people[X[0]]
    while ST:
        now=ST.pop(0)
        for i in road[now]:
            if i in X and visit[i]==0:
                c += people[i]
                ST.append(i)
                visit[i] =1
    for i in X:
        if visit[i] == 0:
            return False
    return c


def back(level,I):
    global result

    box2=[]
    for j in range(1,N+1):
        if j not in box:
            box2.append(j)

    if box and box2:
        a = check(box)
        b = check(box2)
        if a and b:
            if abs(a-b) < result:
                result = abs(a-b)


    for i in range(I,N+1):
        box.append(i)
        back(level+1,i+1)
        box.pop()

N = int(input())
people = [0]+list(map(int,input().split()))
road = {i:[] for i in range(1,N+1)}
for i in range(1,N+1):
    A=list(map(int,input().split()))
    A.pop(0)
    road[i]=A

result = 99999999999
box = []
back(0,1)

if result == 99999999999:
    print(-1)
else:
    print(result)