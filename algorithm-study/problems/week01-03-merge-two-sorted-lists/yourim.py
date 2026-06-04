class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current_node = dummy

        curr1 = list1
        while curr1 is not None:
            while list2 is not None and list2.val <= curr1.val:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next

            current_node.next = curr1
            curr1 = curr1.next
            current_node = current_node.next

        if list2:
            current_node.next = list2

        return dummy.next

#########################################

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next