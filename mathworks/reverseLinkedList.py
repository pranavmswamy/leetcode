# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive version
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # if head is none, return none
        if head == None:
            return None
        # call helper fn
        self.reverse_list(head)
        
        # return collected new head
        return self.headnode
    
    def reverse_list(self, node):
        # if node is none, just return, base case
        if node == None:
            return
        # if node.next is none, it is the last node.
        if node.next == None:
            # make new head node point to this node
            self.headnode = node
            return
        
        self.reverse_list(node.next)
        
        # after it returns to the prev elt, 
        # make node.next.next point to node ( reverse pointing)
        node.next.next = node
        # make node.next = null.
        node.next = None
    

# iterative version
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        prev = None
        
        cur = head
        
        while cur.next != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        cur.next = prev
        return cur
