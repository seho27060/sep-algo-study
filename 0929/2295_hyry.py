import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

twoSum = set()
for i in nums:
    for j in nums:
        twoSum.add(i + j)

ans = 0
for bigIdx in range(N):
    for smallIdx in range(bigIdx):
        if (nums[bigIdx] - nums[smallIdx]) in twoSum:
            ans = max(nums[bigIdx], ans)

print(ans)
