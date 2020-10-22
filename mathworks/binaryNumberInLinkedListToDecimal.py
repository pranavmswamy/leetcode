# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        # Initially thought I have to reverse the list and perform 2^ calc,
        # but theres a smarter way using left shift operator
        # say num = 0.
        # for each node, left shift num by 1 to make way for it,
        # add the value of the node to the number
        # continue
        # this is exactly visualizing the binary number being contructed in num.
        
        num = 0
        while head:
            num = num << 1
            num += head.val
            head = head.next
        
        return num
        
