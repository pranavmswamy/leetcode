class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        
        count = 0
        for i in range(len(s)):
            dp[i][i] = 1
            count += 1
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                count += 1
        
        for i in range(len(s)-3, -1, -1):
            for j in range(len(s)-1, i+1, -1):
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    count += 1
        
        return count


# ANOTHER ALGO, EXPANd around center

class Solution:
    def countSubstrings(self, s: str) -> int:
        # eXPAND from center, two times- once with one center for odd length and once with two centers for even length
        count = 0
        for center in range(len(s)):

            left = center
            right = center
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        
        for center in range(len(s)-1):
            center_left = center
            center_right = center_left + 1
            
            while center_left >= 0 and center_right < len(s):
                if s[center_left] == s[center_right]:
                    count += 1
                    center_left -= 1
                    center_right += 1
                else:
                    break
            
        
        return count
            
               
