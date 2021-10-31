from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if dfs(board, word, [], i, j):
                    return True
        return False
                
def dfs(board, word, visited, i, j):
    m = len(board)
    n = len(board[0])
    
    if word == "":
        return True
    
    if i < 0 or i >= m:
        return False
    if j < 0 or j >= n:
        return False
    
    current_char = word[0]

    if current_char != board[i][j] or (i, j) in visited:
        return False
    
    visited.append((i,j))
        
    if dfs(board, word[1:len(word)], visited, i + 1, j) or \
        dfs(board, word[1:len(word)], visited, i - 1, j) or \
        dfs(board, word[1:len(word)], visited, i, j + 1) or \
        dfs(board, word[1:len(word)], visited, i, j - 1):
        return True
    else:
        visited.pop()
    return False

board = [['A', 'P', 'Q', 'S'], ['T', 'E', 'F', 'W'], ['S','L','U','B'], ['Z','R','E','L']]
dict = ['APE', 'FUEL', 'PET', 'PETS', 'TEA', 'MADAM']

solution = Solution()
print(solution.exist(board, dict[-1]))