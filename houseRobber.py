class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # edge case
        if not nums: return 0
        
        # top down approach
        cache = dict()
        
        def rob_houses(cache, nums, idx):
            if idx in cache:
                return cache[idx]
            else:
                # only one house, return nums[0]
                if idx == 0:
                    return nums[0]
                elif idx == 1:
                    # considering two houses, so return max of those two.
                    return max(nums[0], nums[1])
                else:
                    # either rob current house and current house - 2, or rob current house -1.
                    max_loot = max(nums[idx] + rob_houses(cache, nums, idx-2), rob_houses(cache, nums, idx-1))
                    cache[idx] = max_loot
                    return max_loot
        
        return rob_houses(cache, nums, len(nums)-1)
