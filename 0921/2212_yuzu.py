N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()
lst = []
for i in range(N-1):
    lst.append(arr[i+1]-arr[i])
lst.sort()
print(0) if N<=K else (print(sum(lst[:N-K])))