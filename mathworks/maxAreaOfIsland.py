class Solution:
    # classic dfs,
    # return the count in the dfs instad of void, and keep updating it
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValid(i,j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1
        
        def dfs(i, j):
            if isValid(i, j):
                grid[i][j] = -1
                a = dfs(i, j+1)
                b = dfs(i, j-1)
                c = dfs(i-1, j)
                d = dfs(i+1, j)
                return 1+a+b+c+d
            else:
                return 0
        
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = dfs(i,j)
                    max_count = max(max_count, count)
        
        return max_count
