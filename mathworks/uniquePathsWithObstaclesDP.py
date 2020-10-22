class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # traverse in reverse order, and as soon as you find an obstacle, that and all the ones before it will also become 0
        value = 1
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][-1] == 1:
                value = 0
            dp[i][-1] = value
        
        # traverse in reverse order, and as soon as you find an obstacle, that and all the ones before it will also become 0
        value = 1
        for j in range(n-1, -1, -1):
            if obstacleGrid[-1][j] == 1:
                value = 0    
            dp[-1][j] = value
        
        # if obstacle, value = 0, else, dp recurrence.
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]
