class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board: return False
        
        visited = [[False]*len(board[0]) for i in range(len(board))]
        
        def isValid(board, visited, i, j):
            return i >= 0 and j >=0 and i < len(board) and j < len(board[0]) and visited[i][j] == False
        
        def dfs(board, word, idx, i, j):
            if idx >= len(word):
                return True
            if isValid(board, visited, i, j):
                if board[i][j] == word[idx]:
                    visited[i][j] = True
                    #print(word[idx])
                    a = dfs(board, word, idx+1, i+1, j)
                    if a:
                        return True
                    b = dfs(board, word, idx+1, i-1, j)
                    if b:
                        return True
                    c = dfs(board, word, idx+1, i, j+1)
                    if c:
                        return True
                    d = dfs(board, word, idx+1, i, j-1)
                    if d:
                        return True
                    found = a or b or c or d
                    #if found == False:
                    visited[i][j] = False
                    return found    
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    found = dfs(board, word, 0, i, j)
                    if found: return True
        
        return False
