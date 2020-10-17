class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = dict()
        
        for i in range(len(nums)):
            if target-nums[i] in diction:
                return [i, diction[target-nums[i]]]
            diction[nums[i]] = i
            
        return [-1, -1]


# if input array is sorted, then you can use two pointer approach.
# l + r > target: r--
# elif l+r < target, l++
# else found, return.