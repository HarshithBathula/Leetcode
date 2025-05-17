# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        node, curr = head, head
        
        

        for _ in range(n):
            node = node.next

        if not node:
            return head.next    
        
        while node.next:
            node = node.next
            curr = curr.next

        curr.next = curr.next.next
        return head
        

        node.next = curr  
        return node  


