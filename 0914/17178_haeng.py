N = int(input())
wait = []
people = []

for _ in range(N):
    I = list(input().split())
    for i in range(5):
        new = (I[i][0],int(I[i][2::]))
        I[i] = new
        people.append(new)
    wait.append(I)

ST = []
people.sort()
while wait:
    F = wait.pop(0)

    while F:
        if F[0] == people[0]:
            people.pop(0)
            F.pop(0)
        elif ST and ST[-1] == people[0]:
            people.pop(0)
            ST.pop()
        else:
            if ST and ST[-1] < F[0]:
                print('BAD')
                exit()
            ST.append(F.pop(0))

print('GOOD')
