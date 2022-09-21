N = int(input())
M = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

Chai=[]
if M >= N:
    print(0)
else:
    for i in range(N-1):
        Chai.append(sensor[i+1]-sensor[i])
    Chai.sort()
    result = 0
    for i in range(N-M):
        result += Chai[i]

    print(result)