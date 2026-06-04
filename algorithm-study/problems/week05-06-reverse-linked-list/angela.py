# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr = head #1
        prev = None

        while curr :
            tmp = curr.next #2
            curr.next=prev #None
            prev = curr #1
            curr = tmp #2
        
        return prev