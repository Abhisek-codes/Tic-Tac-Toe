import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout,
    QMessageBox, QInputDialog, QVBoxLayout, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from dal import GameBoard
from bll import GameLogic

ICON_PATH_X = os.path.join("assets", "x.png")
ICON_PATH_O = os.path.join("assets", "o.png")

class TicTacToeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(340, 420)

        self.board = GameBoard()
        self.logic = GameLogic(self.board)
        self.player_scores = {"X": 0, "O": 0}
        self.players = {"X": "Player X", "O": "Player O"}
        self.ai_mode = False

        self.init_game_config()
        self.init_ui()

    def init_game_config(self):
        mode, ok = QInputDialog.getItem(self, "Select Game Mode", "Choose:", ["Player vs Player", "Player vs AI"], 0, False)
        if ok:
            self.ai_mode = (mode == "Player vs AI")

        name1, ok1 = QInputDialog.getText(self, "Player X", "Enter name for Player X:")
        name2 = "Computer" if self.ai_mode else QInputDialog.getText(self, "Player O", "Enter name for Player O:")[0]

        if ok1:
            self.players["X"] = name1
        if name2:
            self.players["O"] = name2

        self.current_player = 'X'

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.score_label = QLabel()
        self.update_score_display()
        main_layout.addWidget(self.score_label)

        self.grid = QGridLayout()
        self.buttons = []

        for i in range(9):
            button = QPushButton("")
            button.setFixedSize(90, 90)
            button.setStyleSheet("background-color: white;")
            button.clicked.connect(lambda _, pos=i: self.handle_move(pos))
            self.buttons.append(button)
            self.grid.addWidget(button, i // 3, i % 3)

        main_layout.addLayout(self.grid)

        controls = QHBoxLayout()
        reset_btn = QPushButton("🔁 Reset Game")
        reset_btn.clicked.connect(self.reset_game)
        quit_btn = QPushButton("❌ Quit")
        quit_btn.clicked.connect(self.close)

        controls.addWidget(reset_btn)
        controls.addWidget(quit_btn)
        main_layout.addLayout(controls)

        self.setLayout(main_layout)

    def handle_move(self, pos):
        if not self.logic.is_valid_move(pos):
            return

        self.play_move(pos, self.current_player)

        if self.logic.check_winner(self.current_player):
            self.player_scores[self.current_player] += 1
            self.update_score_display()
            self.show_message(f"{self.players[self.current_player]} wins!")
            self.reset_board_only()
            return

        if self.logic.is_draw():
            self.show_message("It's a draw!")
            self.reset_board_only()
            return

        self.current_player = 'O' if self.current_player == 'X' else 'X'

        if self.ai_mode and self.current_player == 'O':
            ai_move = self.logic.get_ai_move()
            if ai_move is not None:
                self.handle_move(ai_move)

    def play_move(self, pos, player):
        icon_path = ICON_PATH_X if player == 'X' else ICON_PATH_O
        self.board.update_board(pos, player)
        self.buttons[pos].setIcon(QIcon(icon_path))
        self.buttons[pos].setIconSize(self.buttons[pos].size())

    def update_score_display(self):
        self.score_label.setText(
            f"{self.players['X']} (X): {self.player_scores['X']} | "
            f"{self.players['O']} (O): {self.player_scores['O']}"
        )

    def show_message(self, message):
        QMessageBox.information(self, "Game Result", message)

    def reset_board_only(self):
        self.board.reset_board()
        for btn in self.buttons:
            btn.setIcon(QIcon())
        self.current_player = 'X'

    def reset_game(self):
        self.player_scores = {"X": 0, "O": 0}
        self.update_score_display()
        self.reset_board_only()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeApp()
    window.show()
    sys.exit(app.exec_())
