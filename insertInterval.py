class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,2],[3,5],[6,7],[8,10],[12,16]]
        
        # edge case:
        if not intervals:
            return [newInterval]
        
        # record start_pos(interval to start merging) if intervals[i][1] >= newInterval[0]
        start_pos = -1
        for i in range(0, len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                start_pos = i
                break
        
        # newStartpos will be min(start of new interval, start_pos interval).
        newStart = min(intervals[start_pos][0], newInterval[0])
        
        # if start_pos is still -1, then new interval shd be inserted at the end.
        if start_pos == -1:
            intervals.append(newInterval)
            return intervals
        
        # find end_pos (interval to stop merging)
        # move forward from start_pos until endInterval < intervals[i][0]
        # simultaneously keep updating endInterval to max(endInterval, intervals[i][1] since all those intervals are being merged.)
        newEnd = newInterval[1]
        end_pos = -1
        for i in range(start_pos, len(intervals)):
            if newEnd < intervals[i][0]:
                end_pos = i
                break
            else:
                newEnd = max(newEnd, intervals[i][1])
        
        # if end_pos is still -1, merge from start_pos till end
        if end_pos == -1:
            end_pos = len(intervals)
        
        ans = list()
        # insert till start_pos
        for i in range(0, start_pos):
            ans.append(intervals[i])
            
        # insert merged interval
        ans.append([newStart, newEnd])
        
        # insert from end_interval till end.
        for i in range(end_pos, len(intervals)):
            ans.append(intervals[i])
        
        return ans

    # Beats 84%
                
