#Problem Description:

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]

Output: 6

Example 2:

Input: [1,2,3,4]

Output: 24

Note:

The length of the given array will be in range [3,10^4] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

#Solution:

Time Complexity: O(NlogN)

这道题目没什么可说的。纯粹的数学题目而已。我一开始还想按照几正几负稍微分一下类，后来发现其实没必要。

.. code-block:: python

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

        
