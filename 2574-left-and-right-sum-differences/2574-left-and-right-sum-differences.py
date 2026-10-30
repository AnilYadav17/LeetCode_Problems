class Solution(object):
    def leftRightDifference(self, nums):
        if len(nums) == 0:
            return [0]
        left_sum =[]
        right_sum = []
        lsum = 0
        diff = []
        for i in range(len(nums)):
            rsum = 0
            left_sum.append(lsum)
            for j in range(i+1,len(nums)):
                rsum += nums[j]
            right_sum.append(rsum)
            lsum += nums[i]
        for i,j in zip(left_sum,right_sum):
            diff.append(abs(i-j))
        return diff