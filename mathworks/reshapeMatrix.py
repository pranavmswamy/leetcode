class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if not nums or not nums[0]:
            return nums
        
        if len(nums)*len(nums[0]) != r*c:
            return nums
        
        # else, reshape possible
        
        # iterate over the new matrix
        # oldi, oldj = 0
        # after each copy do oldj += 1
        # if oldj == len(nums[0]), old_i += 1
        # thats all
        
        reshaped_matrix = [[0]*c for _ in range(r)]
        
        old_i = 0
        old_j = 0
        
        for i in range(r):
            for j in range(c):
                reshaped_matrix[i][j] = nums[old_i][old_j]
                old_j += 1
                if old_j == len(nums[0]):
                    old_j = 0
                    old_i += 1
                #if old_i == len(nums):
                 #   break
        
        return reshaped_matrix

# BETTER MATH APPROACH
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if not nums or not nums[0]:
            return nums
        
        if len(nums)*len(nums[0]) != r*c:
            return nums
        
        # else, reshape possible
        
        # BETTER APPROACH - MATH
        # for 2d -> 1d representation, if we know that the 2d array is r*c,
        # then arr[i][j] = arr[i*c + j] (row'th number * len of cols => will give total elts present in the above rows,
        # + c will give the pos of the num in the next row)
        
        # Soooo, for 1d -> 2d,
        # keep a count of the elts added till now, which will simulate a 1d to 2d array
        # [count/c] will give you the row number
        # [count%c] will give you the column number
        # arr[count/c][count%c] = arr[i][j]
        
        reshaped = [[0]*c for _ in range(r)]
        count = 0
        
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                reshaped[int(count/c)][count%c] = nums[i][j]
                count += 1
        
        return reshaped


# ONE LOOP:
'''
public int[][] matrixReshape(int[][] nums, int r, int c) {
    int n = nums.length, m = nums[0].length;
    if (r*c != n*m) return nums;
    int[][] res = new int[r][c];
    for (int i=0;i<r*c;i++) 
        res[i/c][i%c] = nums[i/m][i%m];
    return res;
}

'''
            
