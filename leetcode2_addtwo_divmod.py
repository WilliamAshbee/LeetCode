# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)   # dummy head to simplify result building
        carry = 0
        pointer = head
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, digit = divmod(v1 + v2 + carry, 10) #faster than // and % seperately 

            pointer.next = ListNode(digit)
            pointer = pointer.next

            #traverse list of digits
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
