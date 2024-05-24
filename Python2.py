#TicTacToe game with GUI 

# Using PyQt5 for creating Graphic User Interface

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox

# Defining Segments

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

# Defining Player 'X'
      
        self.board = [[""] * 3 for _ in range(3)]
        self.current_player = "X"

        self.buttons = []
        self.init_ui()

  #Griding and Allignment 

    def init_ui(self):
        layout = QGridLayout()

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = QPushButton("", self)
                button.clicked.connect(lambda _, i=i, j=j: self.on_button_clicked(i, j))
                row_buttons.append(button)
                layout.addWidget(button, i, j)
            self.buttons.append(row_buttons)

        self.setLayout(layout)

  # Push button indexing for the interface

    def on_button_clicked(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            if self.check_winner():
                QMessageBox.information(self, "Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                QMessageBox.information(self, "Tie", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

  # Declaring winner by checking all the boxes

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        self.board = [[""] * 3 for _ in range(3)]
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.setText("")

#Calling of function TicTacToe

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())

# END
