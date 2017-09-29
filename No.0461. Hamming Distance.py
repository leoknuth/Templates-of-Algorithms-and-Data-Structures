class Solution(object):
    def hammingDistance(self, x, y):
        w = x ^ y
        ans = 0
        while w > 0:
            if w % 2 ==1:
                ans = ans +1
            w = w // 2
        return ans
