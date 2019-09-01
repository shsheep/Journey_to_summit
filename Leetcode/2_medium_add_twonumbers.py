# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        
        root = ListNode(None)
        ret = root
        carry = 0
        while l1 or l2:
            if l1 and l2:
                some = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1 and not l2:
                some = l1.val + carry
                l1 = l1.next
            elif not l1 and l2:
                some = l2.val + carry
                l2 = l2.next
            carry = some // 10
            remains = some % 10
            tmp = ListNode(remains)
            root.next = tmp
            root = tmp
        if carry:
            tmp = ListNode(carry)
            root.next = tmp
        return ret.next
                
'''
Runtime: 72 ms, faster than 92.38% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.

'''
