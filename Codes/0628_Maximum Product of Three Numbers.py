class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        p = [0,0,0]
        p[0] = nums[0] * nums[1] * nums[2]
        p[1] = nums[0] * nums[1] * nums[-1]
        p[2] = nums[-1] * nums[-2] * nums[-3]
        return max(p)
        
