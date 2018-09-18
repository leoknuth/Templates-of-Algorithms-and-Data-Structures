#Problem Description:

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

#Solution:

Time Complexity: O(N)

这道题目没什么可说的。根据排序二叉树建立一个有序数组，题目就转化为在一个有序序列里寻找两个数使其和等于目标值。设两个index分别从头和尾向中间扫描即可。

.. code-block:: python

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    class Solution(object):
        def findTarget(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: bool
            """
            # Generate a sorted list from a BST.
            # Then it is almost the same as Problem 0167.

            numbers = self.generate_list(root)

            index1 = 0
            index2 = len(numbers)-1
            target = k
            while (index1 < index2) and (numbers[index1]+numbers[index2] != target):
                if numbers[index1]+numbers[index2] > target:
                    index2 -= 1
                else:
                    index1 += 1

            return (index1 != index2)

        def generate_list(self, root):
            if root:
                return self.generate_list(root.left) + [root.val] + self.generate_list(root.right)
            else:
                return []
