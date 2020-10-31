class Solution:
    
    def generateAdjacentPatterns(self, pattern):
        adjPatterns = list()
        for pos in range(4):
            num = int(pattern[pos])
            str_np_1 = pattern[:pos] + str((num + 1) % 10) + pattern[pos+1:]
            str_np_2 = pattern[:pos] + str((num - 1) % 10) + pattern[pos+1:]
            adjPatterns.append(str_np_1)
            adjPatterns.append(str_np_2)
        return adjPatterns
            
    def bfsOneIteration(self, current_queue, current_set, other_set, deadends):
        
        nextFrontier = list()
        # process current frontier
        for pattern in current_queue:
            # add to current_visited
            # IF YOU ADD NODE TO VISITED HERE, THEN IT WILL BE SLOWER BECAUSE IT HAS TO EXPAND FRONTIER ONE MORE TIME. THIS IS COSTLY IF BRANCHING FACTOR IS HUGE. 
            # current_set.add(pattern)
            
            if pattern in other_set:
                return True, list()
            
            for child in self.generateAdjacentPatterns(pattern):
                if child not in current_set and child not in deadends:
                    # IF YOU ADD NODE TO VISITED OVER HERE,THEN IT WILL PREVENT EXPANSION OF FRONTIER BY ANOTHER LEVEL AND FIND THE TARGET SOONER. (ALWAYS FOLLOW THIS APPROACH)
                    current_set.add(child) # MADE ALL THE TIME DIFF.
                    nextFrontier.append(child)
        
        return False, nextFrontier
            
            
            
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = ['0000']
        end = [target]
        start_set = set()
        end_set = set()
        start_count = 0
        end_count = 0
        
        if target == '0000':
            return 0
        
        if target in deadends or '0000' in deadends:
            return -1
        
        while True:
            if not start or not end:
                return -1
            
            met, next_start = self.bfsOneIteration(start, start_set, end_set, deadends)
            if met: return start_count + end_count
            else: start = next_start
            start_count += 1
            
            met, next_end = self.bfsOneIteration(end, end_set, start_set, deadends)
            if met: return start_count + end_count
            else: end = next_end
            end_count += 1
            
# fASTER THAN 96%
        
