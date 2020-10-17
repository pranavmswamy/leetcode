# WITH SET
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set, res
        res = set()
        
        # sort nums first
        nums.sort()
        
        # for a 3 pair, go upto second last element
        for i in range(len(nums) - 2):
            # if nums[i] > 0, then the sum cannot be 0, so exit loop.
            # exiting loop works because the array is sorted and all elts after nums[i] are sure to be > 0, hence we cannot find a triplet that sums to zero
            if nums[i] > 0:
                break
                
            # continue if the current elt and prev elt are the same, since we are bound to find the same set of triplets again.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # do the usual two pointer approach from i+1 to len(nums)-1 to find the remaining two numbers
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    
                    #while l < r and nums[l] == nums[l+1]:
                    #    l += 1
                    #while l < r and nums[r] == nums[r-1]:
                    #    r -= 1
                    l += 1
                    r -= 1
        
        return res


# WITHOUT SET
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set, res
        res = list()
        
        # sort nums first
        nums.sort()
        
        # for a 3 pair, go upto second last element
        for i in range(len(nums) - 2):
            # if nums[i] > 0, then the sum cannot be 0, so exit loop.
            # exiting loop works because the array is sorted and all elts after nums[i] are sure to be > 0, hence we cannot find a triplet that sums to zero
            if nums[i] > 0:
                break
                
            # continue if the current elt and prev elt are the same, since we are bound to find the same set of triplets again.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # do the usual two pointer approach from i+1 to len(nums)-1 to find the remaining two numbers
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
			# move forward with l if nums[l] and nums[l+1] are the same, since we are bound to find the same values for 2nd and 3rd elt again
                     while l < r and nums[l] == nums[l+1]:
                        l += 1
			# same analogy for right.
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return res
