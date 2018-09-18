class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming
        # dp_max[i] = max(dp_min[i-1]*nums[i],dp_max[i-1]*nums[i],nums[i])
        # dp_min[i] = min(dp_min[i-1]*nums[i],dp_max[i-1]*nums[i],nums[i])
        
        n = len(nums)
        dp_max = [nums[0]] + [0] * (n-1)
        dp_min = [nums[0]] + [0] * (n-1)
        for i in range(1, n):
            dp_max[i] = max(dp_min[i-1]*nums[i], dp_max[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_min[i-1]*nums[i], dp_max[i-1]*nums[i], nums[i])
            
        return max(dp_max)
