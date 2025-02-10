# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        result_head = ListNode()
        if list1.val < list2.val:
            result_head.val = list1.val
            list1 = list1.next
        else:
            result_head.val = list2.val
            list2 = list2.next

        result_current = result_head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                result_current.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                result_current.next = ListNode(val=list2.val)
                list2 = list2.next
            result_current = result_current.next

        while list1 is not None:
            result_current.next = ListNode(val=list1.val)
            list1 = list1.next
            result_current = result_current.next

        while list2 is not None:
            result_current.next = ListNode(val=list2.val)
            list2 = list2.next
            result_current = result_current.next

        return result_head
