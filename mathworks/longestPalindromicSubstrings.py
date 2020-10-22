class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_pal = [[False]*len(s) for i in range(len(s))]
        max_len = 0
        max_pal = ""
        
        # making all i,i's true, single letters true
        for i in range(len(s)):
            is_pal[i][i] = True
        
        for start in range(len(s)-1, -1, -1):
            for end in range(start, len(s), 1):
                if start == end:
                    is_pal[start][end] = True
                elif start + 1 == end:
                    is_pal[start][end] = s[start] == s[end]
                else:
                    is_pal[start][end] = (s[start] == s[end]) and is_pal[start+1][end-1]
                
                if is_pal[start][end] == True and end - start + 1 > max_len:                   
                    max_len = end-start+1
                    max_pal = s[start:end+1]
        
        return max_pal
