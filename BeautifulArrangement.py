class Solution:
    def countArrangement(self, N: int) -> int:
        candidates = dict()
        self.count = 0
        for i in range(1, N+1):
            candidates[i] = list()
            for num in range(1, N+1):
                if i % num == 0 or num % i == 0:
                    candidates[i].append(num)
        
        done = [False]*(N+1)
        
        def recurse(i, candidates, done):
            if i == N+1:
                self.count += 1
                return
            
            for candidate in candidates[i]:
                if not done[candidate]:
                    done[candidate] = True
                    recurse(i+1, candidates, done)
                    done[candidate] = False
        
        recurse(1, candidates, done)
        return self.count
