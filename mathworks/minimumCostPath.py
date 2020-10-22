class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        # dp soln - 
        # cost[i][j] = grid[i][j] + min(cost[i+1][j], cost[i][j+1])
        # variation of the unique paths robot problem. (go down or go right)
        cost = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        cost[len(grid)-1][len(grid[0])-1] = grid[-1][-1]
        
        for j in range(len(grid[0])-2, -1, -1):
            cost[-1][j] = cost[-1][j+1] + grid[-1][j]
        
        for i in range(len(grid)-2, -1, -1):
            cost[i][-1] = cost[i+1][-1] + grid[i][-1]
        
        for i in range(len(grid)-2, -1, -1):
            for j in range(len(grid[0])-2, -1, -1):
                cost[i][j] = grid[i][j] + min(cost[i+1][j], cost[i][j+1])
        
        return cost[0][0]
    
# FASTER THAN 97%
