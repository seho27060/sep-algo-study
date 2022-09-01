import sys
input = sys.stdin.readline

N = int(input())

PR = [0,0,0]
PR2 = [0,0,0]
for i in range(N):
    I = list(map(int,input().split()))

    new = [0,0,0]
    new[0] = max(PR[0],PR[1])+I[0]
    new[1] = max(PR[0],PR[1],PR[2]) + I[1]
    new[2] = max(PR[1],PR[2]) + I[2]
    PR = new

    new = [0,0,0]
    new[0] = min(PR2[0],PR2[1])+I[0]
    new[1] = min(PR2[0],PR2[1],PR2[2]) + I[1]
    new[2] = min(PR2[1],PR2[2]) + I[2]
    PR2 = new

print(max(PR),min(PR2))