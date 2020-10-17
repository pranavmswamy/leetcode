# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2: return ListNode(0)
        if not l1: return l2
        if not l2: return l1
        
        cur = ans = ListNode(0)
        cur1 = l1
        cur2 = l2
        carry = 0
        
        # 1. move both ptrs
        while cur1 and cur2:
            ans_val = carry + cur1.val + cur2.val
            if ans_val >= 10:
                carry = 1
                cur.next = ListNode(ans_val % 10)
            else:
                carry = 0
                cur.next = ListNode(ans_val)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        # 2. move cur1 ptr if cur1
        while cur1:
            ans_val = carry + cur1.val
            if ans_val >= 10:
                carry = 1
                cur.next = ListNode(ans_val % 10)
            else:
                carry = 0
                cur.next = ListNode(ans_val)
            cur = cur.next
            cur1 = cur1.next
        
        # 3. move cur2 ptr if cur2
        while cur2:
            ans_val = carry + cur2.val
            if ans_val >= 10:
                carry = 1
                cur.next = ListNode(ans_val % 10)
            else:
                carry = 0
                cur.next = ListNode(ans_val)
            cur = cur.next
            cur2 = cur2.next
        
        # 4. add carry if carry = 1
        if carry == 1:
            cur.next = ListNode(1)
        
        return ans.next
        
