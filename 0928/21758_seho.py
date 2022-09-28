# 220928 21758 꿀 따기
#  n <= 100,000/ 두마리의 벌꿀이 벌통까지 가면서 채취가능한 벌꿀의 양...

import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
leftToRight = [lst[0]]
for idx in range(1,n):
    leftToRight.append(leftToRight[idx-1]+lst[idx])

A = 0
B = 0
C = 0
for idx in range(1,n-1):
    A = max(A,2*leftToRight[-1]-lst[0]-lst[idx]-leftToRight[idx])
    B = max(B,leftToRight[-1]-lst[-1]-lst[idx]+leftToRight[idx-1])
    C = max(C,leftToRight[idx]-lst[0]+leftToRight[-1]-leftToRight[idx-1]-lst[-1])
print(max(A,B,C))