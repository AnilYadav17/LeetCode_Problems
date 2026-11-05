class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = ''
        for i in words:
            sum = 0
            for j in i:
                init = ord(j) - 97
                sum += weights[init]
            ans += chr(122 - (sum % 26))
        return ans