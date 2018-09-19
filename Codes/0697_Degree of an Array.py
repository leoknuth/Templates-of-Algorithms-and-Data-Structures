class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = {}
        ans = len(nums)
        degree = 0
        for i in range(len(nums)):
            if nums[i] not in val:
                val[nums[i]] = [i,i,1]
            else:
                val[nums[i]][1] = i
                val[nums[i]][2] += 1
            if val[nums[i]][2] > degree:
                ans = val[nums[i]][1] - val[nums[i]][0] + 1
                degree = val[nums[i]][2]
            elif val[nums[i]][2] == degree:
                ans = min(ans, val[nums[i]][1] - val[nums[i]][0] + 1)
        
        return ans