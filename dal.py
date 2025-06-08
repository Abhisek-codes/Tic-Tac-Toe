class GameBoard:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def get_board(self):
        return self.board

    def update_board(self, position, symbol):
        if self.board[position] == ' ':
            self.board[position] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [' ' for _ in range(9)]
