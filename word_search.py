# Given an m x n board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution:
    def search(self, board, word, i, j, index):
        if index == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[index]: 
            return False
        
        temp = board[i][j]
        board[i][j] = ""
        result = (self.search(board, word, i+1, j, index+1) or self.search(board, word, i-1, j, index+1) or self.search(board, word, i, j+1, index+1) or self.search(board, word, i, j-1, index+1))
        board[i][j] = temp
        if result == True:
            print(f"{i} {j}")
        return result
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.search(board, word, i, j, 0):
                    return True
        
        return False
        