# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        slow = head
        fast = head.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next

        return slow
