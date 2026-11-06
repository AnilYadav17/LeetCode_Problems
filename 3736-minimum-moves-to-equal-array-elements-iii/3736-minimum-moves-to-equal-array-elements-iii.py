class Solution(object):
    def minMoves(self, nums):
        result = 0 
        for i in range(len(nums)):
            if nums[i] < max(nums):
                result += max(nums) - nums[i]
        return result
        