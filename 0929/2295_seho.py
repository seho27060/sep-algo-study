# 220929 2295 세 수의 합
import sys

input = sys.stdin.readline

n =int(input())

lst = set()
for _ in range(n):
    lst.add(int(input()))
answer = set()

for s in lst:
    for e in lst:
        answer.add(s+e);
ans= {}

for s in lst:
    for e in lst:
        if (s - e) in answer:
            ans[s]=(s,e,s-e)
answer = sorted(ans.keys(), reverse=True)
print(answer[0])
