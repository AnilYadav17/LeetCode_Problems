class Solution(object):
    def checkDivisibility(self, n):
        digit_sum = 0
        digit_mul = 1
        original = n
        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_mul *= digit
            n = n // 10
        return (original % (digit_mul+digit_sum) == 0)