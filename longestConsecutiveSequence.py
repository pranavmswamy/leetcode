class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to hash set
        # for each number, start checking if num+1 is there in the set,
        # keep track of longest streak. This is O(n^2)
        # To make it O(n), only start checking if num+1 is present if num-1 is not present in the set.
        
        nums_set = set(nums)
        longest_streak = 0
        for num in nums_set:
            if num-1 not in nums_set:
                current_streak = 1
                current_num = num
                
                while current_num+1 in nums_set:
                    current_streak += 1
                    current_num += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
