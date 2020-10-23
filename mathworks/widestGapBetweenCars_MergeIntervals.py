class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort array according to start time.
        # then a linear pass will do
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(interval[1], ans[-1][1])
        
        return ans
