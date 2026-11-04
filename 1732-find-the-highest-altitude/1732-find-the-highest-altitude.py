class Solution(object):
    def largestAltitude(self, gain):
        sum = 0
        altitude = [0]
        for i in range(len(gain)):
            sum += gain[i]
            altitude.append(sum)
        return max(altitude)

        