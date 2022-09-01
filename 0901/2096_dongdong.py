# 백준 2096 내려가기
# 메모리 4mb 제한 - 메초 주의!! => 슬라이딩 윈도우 기법 사용
# 모든 계단의 점수값을 저장하여 배열로 만들면 메모리 초과가 발생
# 슬라이딩 윈도우 - 메모이제이션 할 때 더이상 사용하지 않는 값은 저장하지 않고 배열을 계속해서 갱신해주는 것

N = int(input())

a, b, c = map(int, input().split()) # 일단 첫번째 숫자 받기
max_dp = [a, b, c]  # 최댓값을 저장할 dp 데이터를 계속 받아오면서 갱신해줄거다.
min_dp = [a, b, c]  # 최솟값 dp

# 경우가 세가지 밖에 안나온다. 이차원배열 그려서 생각해보기, 현재 인덱스가 [n][0]일때, [n][1]일때, [n][2]일때

for i in range(1, N):   # 첫번째거는 인풋 받음 두번째부터
    a, b, c = map(int, input().split())
    for j in range(3):
        # 이차원 배열 상 현재 인덱스가 [n][0]일 때 dp배열의 [0]([n-1][0])과 [1]([n-1][1])의 값 활용
        if j == 0:
            max_one = max(max_dp[j], max_dp[j+1]) + a
            min_one = min(min_dp[j], min_dp[j+1]) + a

        # 이차원 배열 상 현재 인덱스가 [n][1]일 때 dp배열의 [0]([n-1][0])과 [1]([n-1][1])과 [2]([n-1][2]) 값 모두 활용
        if j == 1:
            max_two = max(max_dp[j-1], max_dp[j], max_dp[j + 1]) + b
            min_two = min(min_dp[j-1], min_dp[j], min_dp[j + 1]) + b

        # 이차원 배열 상 현재 인덱스가 [n][2]일 때 dp배열의 [1]([n-1][1])과 [2]([n-1][2])의 값 활용
        if j == 2:
            max_thr = max(max_dp[j-1], max_dp[j]) + c
            min_thr = min(min_dp[j-1], min_dp[j]) + c

    max_dp = [max_one, max_two, max_thr]
    min_dp = [min_one, min_two, min_thr]

print(max(max_dp), min(min_dp))


