class Solution(object):
    def minimumSum(self, num):
        digits = sorted(map(int, str(num)))
        return (digits[0] + digits[1]) * 10 + digits[2] + digits[3]