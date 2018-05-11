class Solution:
    """
    @param: board: A list of lists of character
    @param: word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        if not board:
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.existhelper(board, word, col, row):
                    return True
        return False
        
    def existhelper(self, board, word, col, row):
        if len(word) == 0:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[0] != board[row][col]:
            return False
        tmp = board[row][col]
        board[row][col] = "#"
        if self.existhelper(board, word[1:], col+1, row):
            return True
        if self.existhelper(board, word[1:], col-1, row):
            return True
        if self.existhelper(board, word[1:], col, row+1):
            return True
        if self.existhelper(board, word[1:], col, row-1):
            return True
        board[row][col] = tmp
        return False