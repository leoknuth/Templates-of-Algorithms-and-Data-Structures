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
 
