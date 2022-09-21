import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

lst = []
for i in range(1, N):
    lst.append(sensor[i]-sensor[i-1])

lst.sort()
print(sum(lst[:N-K]))