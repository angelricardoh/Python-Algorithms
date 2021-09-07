class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if dfs(board, word, [], i, j):
                    return True
        return False
                
def dfs(board, word, visited, i, j):
    r = len(board)
    c = len(board[0])
    
    if word == "":
        return True
    
    if i<0 or i>=r:
        return False
    if j<0 or j>=c:
        return False
    
    current_char = word[0]

    if current_char != board[i][j] or (i, j) in visited:
        return False
    
    visited.append((i,j))
        
    if dfs(board, word[1:len(word)], visited, i+1, j) or \
        dfs(board, word[1:len(word)], visited, i-1, j) or \
        dfs(board, word[1:len(word)], visited, i, j + 1) or \
        dfs(board, word[1:len(word)], visited, i, j - 1):
        return True
    else:
        visited.pop()
    return False