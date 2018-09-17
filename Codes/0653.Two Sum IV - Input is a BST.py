class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 1
        index2 = len(numbers)
        while (index1 < index2) and (numbers[index1-1]+numbers[index2-1] != target):
            if numbers[index1-1]+numbers[index2-1] > target:
                index2 -= 1
            else:
                index1 += 1
        return [index1,index2]
