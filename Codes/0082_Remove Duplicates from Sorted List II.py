# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # I hate pointers!
        # Attention! It is a sorted linked list.
        # Attention! head may be None (The Input data may be an empty list).
        if head == None:
            return None
        ans_head = None
        ans_cur = ans_head
        
        pre_val = head.val - 1
        cur_point = head
        
        while cur_point:
            cur_val = cur_point.val
            if cur_val != pre_val:
                if (cur_point.next == None) or (cur_val != cur_point.next.val):
                    if ans_head == None:
                        ans_head = ListNode(cur_val)
                        ans_cur = ans_head
                    else:
                        ans_cur.next = ListNode(cur_val)
                        ans_cur = ans_cur.next
            pre_val = cur_val
            cur_point = cur_point.next
        
        return ans_head
            
            
        
        
