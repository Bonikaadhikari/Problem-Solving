#LeetCode Two Sum Problem
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if(nums[i]+nums[j] == target and i != j):
                return [i, j]
result = twoSum([2, 3, 8, 5], 8)
print(result)