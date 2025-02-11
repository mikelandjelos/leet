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
        if head is None:
            return head

        prev = None
        curr = head
        next = head.next

        while next is not None:
            temp = next.next

            curr.next = prev
            next.next = curr
            prev = curr
            curr = next
            next = temp

        return curr
