class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = dict()
        return self.coin_bottom_up(coins, amount)
        
        # USUAL DP RECURRENCE WITH EDGE CASES-
        # DP[0] = 0
        # DP[I] = MIN(1+DP[I-COIN] FOR COIN IN COINS IF I-COIN >= 0 AND DP[I-COIN] != -1)
        
        
    def coin_top_down(self, coins, amount, cache):
        if amount in cache:
            return cache[amount]
        
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        else:
            candidates= list()
            for coin in coins:
                sub_problem = self.coin_top_down(coins, amount-coin, cache)
                if sub_problem != -1:
                    candidates.append(sub_problem+1)
            if candidates:
                cache[amount] = min(candidates)
            else:
                cache[amount] = -1
            return cache[amount]
    
    def coin_bottom_up(self, coins, amount):
        dp = [0]*(amount+1)
        
        #for i in range(1, min(coins)):
        #    dp[i] = -1
        dp[0] = 0
        
        for i in range(1, len(dp)):
            arr = [1+dp[i-coin] for coin in coins if i-coin >= 0 and dp[i-coin] != -1]
            if arr:
                dp[i] = min(arr)
            else:
                dp[i] = -1
        
        return dp[-1]
        
        
        
        
