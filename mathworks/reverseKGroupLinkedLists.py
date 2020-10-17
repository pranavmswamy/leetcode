# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # reverse_ll helper function
    def reverse_ll(self, node):
        self.new_head = None
        #print("Node - ", node)
        def reverse(node):
            if not node.next:
                self.new_head = node
                return
            reverse(node.next)
            node.next.next = node
            node.next = None
        
        reverse(node)
        #print("New head", self.new_head)
        return self.new_head
    
    # give the start node and end node as input, returns the reversed ll.
    def reverse_k(self, start_node, end_node):
            # severing the list
            end_node.next = None
            
            #print("Reverse-k,", start_node,"---", end_node)
            new_head = self.reverse_ll(start_node)
            return new_head
    
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        # traverse until the kth node, and then reverse until there
        # put the head in a list
        # traverse from k+1th node, ...
        # while traversing if it does not reach k nodes, just add that unreversed head to the list
        
        # combine the elements in the list by iterating through the lists and then return the answer
        
        # edge case
        if not head:
            return None
        
        list_of_ll = list()
        
        cur = head
        
        while cur != None:
            # start counting k
            kcount = 1
            start_node = cur
            kcur = start_node
            
            # stops at exactly the kth node
            while kcur.next != None and kcount < k:
                kcur = kcur.next
                kcount += 1
            
            # if kcount < k, we reached the end sooner, so just add start node, break
            if kcount < k:
                list_of_ll.append(start_node)
                break
            else:
                # else, collect kcur.next in temp var since I am severing the list.
                # append the reverse of start node-> endnode to list_of_ll
                temp = kcur.next
                list_of_ll.append(self.reverse_k(start_node, kcur))
                
                # continue for the next set of k nodes by making cur = temp
                cur = temp
        
        #print(list_of_ll)
        
        # combine all the reversed lls in the list.
        head = list_of_ll[0]
        for i in range(len(list_of_ll) - 1):
            cur = list_of_ll[i]
            while cur.next != None:
                cur = cur.next
            cur.next = list_of_ll[i+1]
        
        return head
                
# FASTER THAN 98%
