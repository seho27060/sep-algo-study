# 백준 2251 물통

from collections import deque


def bfs():
    while Q:
        x, y, z = Q.popleft()

        if visited[x][z] == 1:  # 방문 체크
            continue
        else:
            visited[x][z] = 1

        if x == 0:  # A 물 컵이 비어있다면
            C_check[z] = 1  # C 물 양 체크 배열을 1로 바꿔준다

        # 경우의 수는 6가지  A -> B, C or B -> A, C or C -> A, B 모든 경우의 수 나눠서 생각하기
        # 경우의 수를 잘 생각하자....

        # A -> B
        if x + y > B:  # B 가 넘칠 때
            Q.append([x + y - B, B, z])  # 나눠서 담아주기
        else:  # 아니면
            Q.append([0, x + y, z])  # A -> B를 해서 A를 0으로 만들어준다

        # A -> C
        if x + z > C:  # C가 넘칠 때
            Q.append([x + y - C, y, C])  # 나눠서 담아주기
        else:  # 아니면
            Q.append([0, y, x + z])  # A -> C를 해서 A를 0으로 만들기

        # B -> A
        if y + x > A:  # A가 넘치면
            Q.append([A, y + x - A, z])  # 나눠담기
        else:  # 아니면
            Q.append([y + x, 0, z])  # B를 0으로 만들기

        # B -> C
        if y + z > C:  # C가 넘치면
            Q.append([x, y + z - C, C])  # 나눠담기
        else:  # 아니면
            Q.append([x, 0, y + z])  # B를 0으로 만들기

        # C -> A
        if z + x > A:
            Q.append([A, y, z + x - A])
        else:
            Q.append([z + x, y, 0])

        # C -> B
        if z + y > B:
            Q.append([x, B, z + y - B])
        else:
            Q.append([x, z + y, 0])


A, B, C = map(int, input().split())
Q = deque()
Q.append([0, 0, C])
visited = [[0] * (201) for _ in range(C + 1)]  # 방문 체크 리스트
C_check = [0 for _ in range(C + 1)]  # C 물컵 양 체크 리스트

bfs()

# print(C_check)
for i in range(len(C_check)):
    if C_check[i] == 1:
        print(i, end=" ")
