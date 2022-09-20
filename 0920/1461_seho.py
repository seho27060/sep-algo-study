# 220920 1461 도서관
# 한번의 m개의 책을 들고 각 위치로 둬야함,, 완료시점 걸음수는?
# 정렬하고 음수/양수 파트로 나누기
# 파트에서 큰수부터 m개씩 자르고 해당 집합에서 절댓값 가장 큰수 가 대표수
# 양 파트에 m개로 구성된 부분집찹의 대표수 추출
# 대표수 리스트에서 가장 큰수는 *1, 나머지 수 합 * 2 의 합이 답.
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
lst = sorted(map(int,input().split()))
result = set()
start = 0

before = []
after = []
for l in lst:
    if l < 0:
        before.append(l)
    else:
        after.append(l)
# print(before)
after.reverse()
# print(after)

idx = 0
while idx < len(before):
    result.add(before[idx])
    idx += m
idx = 0
while idx < len(after):
    result.add(after[idx])
    idx += m

result = sorted(result)

maxIdx = -1
maxValue = -1
for idx in range(len(result)):
    if maxValue < abs(result[idx]):
        maxValue = abs(result[idx])
        maxIdx = idx
answer = 0
for idx in range(len(result)):
    if idx == maxIdx:
        answer += abs(result[idx])
    else:
        answer += abs(result[idx])*2
print(answer)
