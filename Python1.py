Calculator Making Sound as You Type
Python Code

#pip install pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QSoundEffect

#importing all necessary libraries

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.input_line = QLineEdit()
        self.input_line.setReadOnly(True)
        self.input_line.setAlignment(Qt.AlignRight)
        self.input_line.setFont(QFont("Arial", 14))
      
      # Defining GUI interface for font and allignment

        self.create_buttons()

#creating buttons with layout in rows and columns
      
        layout = QVBoxLayout()
        layout.addWidget(self.input_line)
        for row in self.buttons:
            h_layout = QHBoxLayout()
            for button in row:
                h_layout.addWidget(button)
            layout.addLayout(h_layout)

        self.setLayout(layout)

        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile("snd_fragment_retrievewav-14728.wav"))
        self.sound_effect.setVolume(1.0)  # Set volume to maximum

    def create_buttons(self):
        self.buttons = [
            [
                QPushButton("7"), QPushButton("8"), QPushButton("9"), QPushButton("/")
            ],
            [
                QPushButton("4"), QPushButton("5"), QPushButton("6"), QPushButton("*")
            ],
            [
                QPushButton("1"), QPushButton("2"), QPushButton("3"), QPushButton("-")
            ],
            [
                QPushButton("0"), QPushButton("."), QPushButton("C"), QPushButton("+")
            ],
            [
                QPushButton("=")
            ]
        ]

      # Defining GUI interface for buttons and push signals
      
        for row in self.buttons:
            for button in row:
                button.clicked.connect(self.button_click)

    def button_click(self):
        button = self.sender()
        text = button.text()

        self.sound_effect.play()

        if text == "=":
            expression = self.input_line.text()
            try:
                result = eval(expression)
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText("Error")
        elif text == "C":
            self.input_line.clear()
        else:
            self.input_line.insert(text)
# Defining error promt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

#End
