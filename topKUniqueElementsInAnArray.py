class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # initial thought
        # BUILD MAX HEAP - O(n)
        # KEEP REMOVING TOP ELT UNTIL K UNIQUE ELTS ARE REACHED. - log(n) + log(n) + ... + log(n) until k unique elts are reached.
        
        # BETTER VERSION
        # Keep map of elt -> count - O(n)
        # Insert k elts into min heap, with key as count. - (O(k))
        # After that, insert and delete-min the rest of the elts. (O((n-k)lgk)
        # At the end, top k unique elts remain. Return those.
        
        
        from collections import Counter
        count_dict = Counter(nums)
        
        k_list = [(count, value) for value, count in count_dict.items()]
        
        ans = []
        
        i = 0
        while i < k:
            heapq.heappush(ans,k_list[i])
            i += 1
        
        while i < len(k_list):
            heapq.heappushpop(ans, k_list[i])
            i += 1
        
        return [i[1] for i in ans] 
