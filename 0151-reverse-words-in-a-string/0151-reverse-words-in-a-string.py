class Solution(object):
    def reverseWords(self, s):
        s = s.split(" ")
        print(s)
        rev = []
        for i in s:
            if i!="":
                rev.append(i)
        return(' '.join(rev[::-1]))