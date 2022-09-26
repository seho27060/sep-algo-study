# 백준 1976 여행가자 - 유니온 파인드
'''
유니온파인드 알고리즘 - 여러 노드가 존재할 때 어떤 두 개의 노드를 같은 집합으로 묶어주고,
다시 어떤 두 노드가 같은 집합에 있는지 확인하는 알고리즘
find - 노드 x 가 어느 집합에 포함되어 있는지 찾는 연산 부모노드를 찾을 때까지 재귀적으로 호출한다
union - 노드 x 가 포함된 집합과 노드 y 가 포함된 집합을 합치는 연산 두 원소의 부모노드를 찾고 번호가 큰 노드가 번호가 작은
노드의 번호를 가리키도록 한다
'''

# 여행 했던 곳을 다시 여행하는 부분을 처리하기 위해 유니온 파인드를 사용??
# 내가 도시를 갈 수 있냐 없냐만 판단을 하면 된다 -> 내가 갈 도시들이 같은 루트 노드를 가지고 있는지 확인

# x가 속한 집합과 y가 속한 집합 합치기
def union(x, y):
    x = find(x) # x노드의 부모 노드 찾기
    y = find(y) # y노드의 부모 노드 찾기

    # x와 y의 부모노드가 같으면 동일한 집합이므로 리턴
    if x == y:
        return

    if x < y:   # x의 부모가 y 부모보다 상위루트라면
        parent[y] = x   # y의 부모를 x의 부모로 변경
    else:   # y의 부모가 x부모보다 상위루트이면
        parent[x] = y   # x의 부모를 y의 부모로 변경

# 부모 노드 찾기
def find(target):
    # 자기 자신이 부모노드라면 자기 자신 그냥 리턴
    if target == parent[target]:
        return target

    # 부모 노드를 재귀함수로 찾기 target노드를 따라가면서 찾는다
    p = find(parent[target])
    parent[target] = p  # 부모 테이블 갱신

    # 자신의 부모 노드를 리턴
    return parent[target]

N = int(input())    # 도시의 수 = 노드의 수
M = int(input())    # 여행계획에 속한 도시 수 = 정점의 수

parent = [0] * (N+1)    # 부모테이블 union연산을 하기 위해서는 부모테이블이 있어야 함 외우자
for x in range(1, N+1):     # 부모 테이블 상에서 부모를 자기 자신으로 초기화
    parent[x] = x

for i in range(1, N+1): # i번째 도시
    graph = list(map(int, input().split())) # i번째 도시가 어느 도시와 연결되어 있는지에 대한 정보
    # i도시와 연결되어 있는 도시를 확인
    for j in range(1, len(graph)+1):
        # print(graph[j-1])
        if graph[j-1] == 1:     # j도시와 연결되어 있다면... 이게 왜 연결이지 근데?? - graph에서 1이 연결되었단 뜻임 빡대가리세요..??
            union(i, j)     # 연결 되어 있다면 두 도시를 합집합으로 표현

plan = list(map(int, input().split()))

ans = set([find(i) for i in plan])  # set함수로 합집합 찾기, 여행계획의 루트노드를 찾는 것

if len(ans) == 1:
    print('YES')
else:
    print('NO')     # set개수가 1이 아니면 두개의 집합이 존재하는 것 -> 모든 도시 방문 불가


