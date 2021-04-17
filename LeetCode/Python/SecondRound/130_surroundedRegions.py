def solve(self, board: List[List[str]]) -> None:

    if len(board) == 0 or len(board[0]) == 0:
        return
    
    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        if board[row][0] == "O":
            self.dfs(board, row, 0, rows, cols)
        if board[row][cols - 1] == "O":
            self.dfs(board, row, cols - 1, rows, cols)
    
    for col in range(cols):
        if board[0][col] == "O":
            self.dfs(board, 0, col, rows, cols)
        if board[rows - 1][col] == "O":
            self.dfs(board, rows - 1, col, rows, cols)
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "O":
                board[row][col] = "X"
            elif board[row][col] == "*":
                board[row][col] = "O"

def dfs(self, board, row, col, rows, cols):

    if row >= 0 and col >= 0 and row < rows and col < cols and board[row][col] == "O":
        board[row][col] = "*"
        self.dfs(board, row + 1, col, rows, cols)
        self.dfs(board, row - 1, col, rows, cols)
        self.dfs(board, row, col - 1, rows, cols)
        self.dfs(board, row, col + 1, rows, cols)
    else:
        return