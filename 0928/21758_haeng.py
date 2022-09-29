# 지각 죄송합니다 푼줄알았어요ㅠㅠ

def beeD(s,e):
    c = 0
    ans = 0
    X = LINE[s]
    for i in range(s+1,e+1):
        c += LINE[i]
        if c >= X: break
        D = X-LINE[i] -c
        if D > ans:
            ans = D
    return ans

def beeR(s,e):
    c = 0
    ans = 0
    X = LINE[e]
    for i in reversed(range(s,e)):
        c += LINE[i]
        if c >= X: break
        D = X-LINE[i] -c
        if D > ans:
            ans = D
    return ans

N = int(input())
LINE = list(map(int,input().split()))

result = 0
S = sum(LINE)
L = 0
R = sum(LINE)-LINE[-1]-LINE[-2]
for i in range(N):
    if i == 0:
        A = S*2 -LINE[-1]*2-LINE[-2]*2 + beeR(1,N-2)
        if A > result:
            result=A
    elif i == N-1:
        A = S*2 -LINE[0]*2-LINE[1]*2 + beeD(1,N-2)
        if A > result:
            result = A
    else:
        if i >=2: L += LINE[i]

        A = R*2 + beeR(i+1,N-2)
        B = L*2 + beeD(1,i-1)
        C = S - LINE[0] - LINE[-1] + LINE[i]
        result = max(A,B,C,result)

        R -= LINE[i]

print(result)