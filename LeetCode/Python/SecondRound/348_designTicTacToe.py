class TicTacToe:

    def __init__(self, n):
        self.rows = [0 for x in range(n)]
        self.cols = [0 for x in range(n)]
        self.diagonal = 0
        self.antiDiagonal = 0
    
    def move(self, row, col ,player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        playerMark == 1 if player == 1 else -1
        self.rows[row] += playerMark
        self.cols[col] += playerMark

        if row == col:
            self.diagonal += playerMark
        
        if row == len(self.rows) - 1 - col:
            self.antiDiagonal += playerMark

        return self.winner(row, col, player)
    
    def winner(self, row, col, player):
        
        victoryPoint = len(self.rows)

        if abs(self.rows[row]) == victoryPoint or \
           abs(self.cols[col]) == victoryPoint or \
           abs(self.diagonal) == victoryPoint or \
           abs(self.antiDiagonal) == victoryPoint:

           return player
        
        return 0