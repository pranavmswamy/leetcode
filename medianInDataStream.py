# METHOD 1 - Using a min heap to store seond half elts, using a max-heap to store first half elts
# Median will be extract(maxheap) if n is odd, (extract(maxheap) + extract(minheap)) / 2 if n is even.

# To add elts:
# first add num to maxheap
# then extractmax(maxheap) and add it to min_heap
# if len(minheap) > len(maxheap), then extractmin(minheap) and offer to maxheap.

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = list()
        self.min_heap = list()
        
    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+ self.min_heap[0]) / 2
        

# insert - logn, 
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
