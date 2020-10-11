# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Many approaches in decreasing order of time complexity.
        # 0. collect all values, sort, create LL (O(NlgN)) , bruteforce
        # 1. compare two at a time (O(Nk))
        # 2. compare k nodes in all k lls. (O(Nk))
        # 3. compare with divide and conquer (pair up lists and compare): (O(Nlogk))
        # 4. use a min heap of size k and keep pushing from wherever you extractmin - O(Nlogk)
        
        # trying method 4.
        
        # init list with first node from all lls
        heap = [(ll.val, idx) for idx, ll in enumerate(lists) if ll]
        
        # heapify the list
        heapq.heapify(heap)
        
        head = ListNode(0)
        cur = head
        # repeat till heap is empty
        while heap:
            # pop smallest element
            val, idx = heapq.heappop(heap)
            
            # create node of val and attach it to ans ll.
            cur.next = ListNode(val)
            # move cur
            cur = cur.next
            
            # update heap
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            
        return head.next
    
# Faster than 97%
