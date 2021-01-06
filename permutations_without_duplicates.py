class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # soln 1 - using set
        # self.ans = set()
        self.ans_list = list()
        self.permute(nums, list());
        return self.ans_list
    
#     def permute(self, nums, cur):
#         if not nums:
#             self.ans.add(tuple(cur))
        
#         for i in range(len(nums)):
#             self.permute(nums[:i] + nums[i+1:], cur + [nums[i]])
    
    # soln 2 w/o using set
    def permute(self, nums, cur):
        if not nums:
            self.ans_list.append(cur)
        
        # have to do len(nums) recursive calls, but only for unique ones, since dup ones will produce dup result.
        for i in range(0, len(nums)):
            if self.should_skip(nums, i):
                continue
            else:
                self.permute(nums[:i] + nums[i+1:], cur + [nums[i]])
    
    # fn to check if there are any positions before i that have the same val as nums[i] in order to skip the recursive call.
    def should_skip(self, nums, i):
        for j in range(i):
            if nums[j] == nums[i]:
                return True
        return False

<< EOF


