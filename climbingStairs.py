class Solution:
    
    def __init__(self):
        self.climb_dict = dict()
    
    def climbStairs(self, n: int) -> int:
        # Top Down approach DP
        
        # base cases
        if n < 0:
            return 0
        if n == 0:
            # one way to climb 0th step- be there.
            return 1
        
        # memoized case
        if n in self.climb_dict:
            return self.climb_dict[n]
        
        # calculate if not memoized
        # no. of ways to go to climb n stairs = no. of ways to climb n-1 stairs + no. of ways to climb n-2 stairs. (No +1 since its all converging to the nth step, so it will be the same)
        n_stairs = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.climb_dict[n] = n_stairs
        return n_stairs
