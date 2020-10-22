class Solution:
    def __init__(self):
        self.fibvals = {0:0, 1:1}
        
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        if N in self.fibvals:
            return self.fibvals[N]
        else:
            ans = self.fib(N-1) + self.fib(N-2)
            self.fibvals[N] = ans
            return ans
