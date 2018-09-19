import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        n, m, p = buckets, minutesToDie, minutesToTest
        ans = int(math.ceil(math.log(n)/math.log(math.trunc(p/m) + 1)))
        return ans
