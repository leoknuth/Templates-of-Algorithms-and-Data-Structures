#Problem Description:

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.


#Solution:

Time Complexity: O(N)

这道题目对我来说挺难的。这道数学题，挺考验分析能力和智商的。

我一开始以为和二进制有关。结果想了很久没做出来。

然后我就去看了Stefan Pochmann大神写的解答。大神真的时又聪明又能把事情讲的十分清晰！

With 2 pigs, poison killing in 15 minutes, and having 60 minutes, we can find the poison in up to 25 buckets in the following way. Arrange the buckets in a 5×5 square:

 :: 

     1  2  3  4  5
     6  7  8  9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25

Now **use one pig to find the row** (make it drink from buckets 1, 2, 3, 4, 5, wait 15 minutes, make it drink from buckets 6, 7, 8, 9, 10, wait 15 minutes, etc). **Use the second pig to find the column** (make it drink 1, 6, 11, 16, 21, then 2, 7, 12, 17, 22, etc).

Having 60 minutes and tests taking 15 minutes means we can run four tests. If the row pig dies in the third test, the poison is in the third row. If the column pig doesn't die at all, the poison is in the fifth column (this is why we can cover five rows/columns even though we can only run four tests).

With 3 pigs, we can similarly use a 5×5×5 cube instead of a 5×5 square and again use one pig to determine the coordinate of one dimension (one pig drinks layers from top to bottom, one drinks layers from left to right, one drinks layers from front to back). So 3 pigs can solve up to 125 buckets.

In general, we can solve up to (⌊minutesToTest / minutesToDie⌋ + 1)^pigs buckets this way, so just find the smallest sufficient number of pigs for example like this:

.. code-block:: python

    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

另外，听说大神归隐热带雨林了？

.. code-block:: python

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
