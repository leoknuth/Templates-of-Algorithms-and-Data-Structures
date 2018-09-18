#Problem Description:

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example:

Input: [2,3,-2,4]

Output: 6

Explanation: [2,3] has the largest product 6.

#Solution:

Time Complexity: O(N)

这道题目没什么可说的。一般和数列有关，和最大最小值有关，和连续取值有关，都要优先思考动态规划。

.. code-block:: python

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
