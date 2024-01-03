#Remove Duplicate from sorted array
class Solution:
    def removeDuplicates(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if(nums[j] != nums[i]):
                j +=1
                nums[j] = nums[i]
        return j +1
result = Solution() 
r = result.removeDuplicates([1,1,2,3,3,4,5,6,6,7])
print(r)