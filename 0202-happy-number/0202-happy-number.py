class Solution(object):

    def part_result(self, n):
        total = 0

        for i in str(n):
            total += int(i) ** 2

        return total

    def isHappy(self, n):
        while True:
            n = self.part_result(n)
            if n == 1 :
                return True
            if n == 4 :
                return False

            