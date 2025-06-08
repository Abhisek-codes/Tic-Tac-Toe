import math

class GameLogic:
    def __init__(self, board):
        self.board = board

    def check_winner(self, symbol):
        b = self.board.get_board()
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for cond in win_conditions:
            if b[cond[0]] == b[cond[1]] == b[cond[2]] == symbol:
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board.get_board()

    def is_valid_move(self, position):
        return self.board.get_board()[position] == ' '

    def get_ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board.get_board()[i] == ' ':
                self.board.get_board()[i] = 'O'
                score = self.minimax(False)
                self.board.get_board()[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, is_maximizing):
        if self.check_winner('O'):
            return 1
        if self.check_winner('X'):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board.get_board()[i] == ' ':
                    self.board.get_board()[i] = 'O'
                    score = self.minimax(False)
                    self.board.get_board()[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board.get_board()[i] == ' ':
                    self.board.get_board()[i] = 'X'
                    score = self.minimax(True)
                    self.board.get_board()[i] = ' '
                    best_score = min(score, best_score)
            return best_score
