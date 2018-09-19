#Problem Description:

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example:

Input: [1, 2, 2, 3, 1]

Output: 2

Explanation: 

The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

#Solution:

Time Complexity: O(N)

这道题目没什么可说的。开个字典（或集合）记录每个值出现的次数、最初位置、最末位置即可。

.. code-block:: python

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