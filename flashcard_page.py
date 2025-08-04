from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class FlashcardPage(QWidget):
    def __init__(self):
        super().__init__()

        self.flashcards = [
            {
                "question": "What is the capital of France?",
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "answer": "Mars"
            },
            {
                "question": "What is the boiling point of water?",
                "answer": "100°C"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "answer": "William Shakespeare"
            }
        ]

        self.current_index = 0
        self.answer_visible = False

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Question Label
        self.question_label = QLabel()
        self.question_label.setFont(QFont("Georgia", 22, QFont.Bold))
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setWordWrap(True)
        layout.addWidget(self.question_label)

        # Answer Label (hidden initially)
        self.answer_label = QLabel()
        self.answer_label.setFont(QFont("Arial", 18))
        self.answer_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setStyleSheet("color: #2980b9; padding-top: 15px;")
        self.answer_label.setWordWrap(True)
        self.answer_label.hide()
        layout.addWidget(self.answer_label)

        # Buttons box for navigation and show/hide answer
        btn_layout = QHBoxLayout()

        self.btn_prev = QPushButton("← Previous")
        self.btn_prev.setFixedWidth(120)
        self.btn_prev.clicked.connect(self.prev_card)
        btn_layout.addWidget(self.btn_prev)

        self.btn_show_hide = QPushButton("Show Answer")
        self.btn_show_hide.setFixedWidth(140)
        self.btn_show_hide.clicked.connect(self.toggle_answer)
        btn_layout.addWidget(self.btn_show_hide)

        self.btn_next = QPushButton("Next →")
        self.btn_next.setFixedWidth(120)
        self.btn_next.clicked.connect(self.next_card)
        btn_layout.addWidget(self.btn_next)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.load_card()

    def load_card(self):
        card = self.flashcards[self.current_index]
        self.question_label.setText(card["question"])
        self.answer_label.setText(card["answer"])

        # Reset answer visibility and button text
        self.answer_visible = False
        self.answer_label.hide()
        self.btn_show_hide.setText("Show Answer")

        # Disable prev button if at start
        self.btn_prev.setEnabled(self.current_index > 0)
        # Disable next button if at end
        self.btn_next.setEnabled(self.current_index < len(self.flashcards) - 1)

    def toggle_answer(self):
        if self.answer_visible:
            self.answer_label.hide()
            self.btn_show_hide.setText("Show Answer")
            self.answer_visible = False
        else:
            self.answer_label.show()
            self.btn_show_hide.setText("Hide Answer")
            self.answer_visible = True

    def next_card(self):
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            self.load_card()

    def prev_card(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_card()
