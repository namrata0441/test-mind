from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets # Explicitly import QtWidgets for QApplication

class QuizWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel("<h2>Quizze Page Content Goes Here</h2>")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quiz_widget = QuizWidget()
    quiz_widget.show()
    sys.exit(app.exec_())
