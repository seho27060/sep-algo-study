import sys

sys.setrecursionlimit(10 **5)

input = sys.stdin.readline
def dfs(s):
    global ans
    st.append(s)
    v[s] = 1
    c = lst[s]
    if v[c]:
        if c in st:
            ans += st[st.index(c):]

        return
    else:
        dfs(c)


TC = int(input())
for _ in range(TC):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    v = [0] * (n+1)
    ans = []

    for i in range(1, n+1):
        if v[i] == 0:
            st = []
            dfs(i)
    print(n -len(ans))
