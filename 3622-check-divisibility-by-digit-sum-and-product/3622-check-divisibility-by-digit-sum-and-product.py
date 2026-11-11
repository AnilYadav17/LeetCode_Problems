class Solution(object):
    def checkDivisibility(self, n):
            return n % (reduce(lambda x, y: x + y, map(int, str(n))) + reduce(lambda x, y: x * y, map(int, str(n)))) == 0

        