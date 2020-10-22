class Solution:

# O(2n) space.
    def uniquePaths(self, m: int, n: int) -> int:
        # clasic dp problem.
        
        dp = [[0]*2 for _ in range(m)]
        
        for i in range(m):
            dp[i][-1] = 1
        
        for j in range(2):
            dp[-1][j] = 1
        
        
        repeat_times = 0
       # print(dp)
        
        while repeat_times != n-1:
            #print(dp[0],"\n",dp[1],"\n",dp[2],"\n")
            for i in range(m-2, -1, -1):
                dp[i][0] = dp[i+1][0] + dp[i][1]

            for i in range(m-1, -1, -1):
                dp[i][1] = dp[i][0]
            
            dp[-1][0] = 1
            for i in range(m-2, -1, -1):
                dp[i][0] = 0
            repeat_times += 1
            
        return dp[0][1]
