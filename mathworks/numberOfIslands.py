class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # classic dfs
        if not grid:
            return 0
        
        self.visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        def dfs(i, j):
            if isValid(i, j):
                self.visited[i][j] = True
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)
        
        def isValid(i,j):
            if i >= 0 and j>=0 and i <len(grid) and j <len(grid[0]) and self.visited[i][j] == False and grid[i][j] == '1':
                return True
            return False
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.visited[i][j] == False and grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        
        return count
