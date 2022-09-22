N = int(input())
nums = list(map(int, input().split()))

numDic = dict()
cnt = dict()
for num in nums:
    cnt[num] = cnt.get(num, 0) + 1

for i in range(1, N):
    for j in range(i):
        if nums[i] == 0 and nums[j] == 0:
            if cnt[0] > 2:
                numDic[nums[i] + nums[j]] = numDic.get(nums[i] + nums[j], 0) + 1
        elif (nums[i] == 0 and nums[j] != 0) or (nums[i] != 0 and nums[j] == 0):
            if cnt[nums[i] + nums[j]] > 1:
                numDic[nums[i] + nums[j]] = numDic.get(nums[i] + nums[j], 0) + 1
        else:
            numDic[nums[i] + nums[j]] = numDic.get(nums[i] + nums[j], 0) + 1

ans = 0
for num in nums:
    if num in numDic: ans += 1

print(ans)
