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


# w/o using dict

class Solution:
    def countArrangement(self, N: int) -> int:
        
        def recurse(pos, done):
            if pos == N+1:
                self.count += 1
                return
            
            for num in range(1, N+1):
                if not done[num] and (num%pos == 0 or pos%num == 0):
                    done[num] = True 
                    recurse(pos+1, done)
                    done[num] = False
        
        
        done = [False]*(N+1)
        self.count = 0
        recurse(1, done)
        return self.count
