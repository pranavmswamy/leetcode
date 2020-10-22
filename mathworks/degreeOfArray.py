class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # collect leftmost idx, rightmost idx, count of all elements.
        # find max frequency
        # then, for all elts with max_freq,
        # find out min subarray length by doing min(min_subarray_len, right[num] - left[num] + 1)
        
        
        # contains all left most indices of an elt in the array
        left = dict()
        
        # contains all the right most indices of an elt in the array
        right = dict()
        
        # count of all nums
        count = dict()
        
        max_count = 0
        
        
        # populate left, right, count, max_count
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
            
            if count[nums[i]] > max_count:
                max_count = count[nums[i]]
        
        # collect all max_keys
        max_keys = [key for key,val in count.items() if val == max_count]
        
        # find min distance of all max keys.
        min_subarray_len = len(nums)
        for num in max_keys:
            min_subarray_len = min(min_subarray_len, right[num] - left[num]+1)
            
        return min_subarray_len
            
