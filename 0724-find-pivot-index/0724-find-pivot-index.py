class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[i+1:]) == sum(nums[:i]):
                return i
        else:
            return -1