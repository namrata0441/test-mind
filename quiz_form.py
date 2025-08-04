import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLabel, QRadioButton, QPlainTextEdit, QGroupBox, QSpinBox, QMessageBox
from PyQt5.QtCore import Qt
import random

from quiz_ui import Ui_MainWindow as QuizUi_MainWindow_Generated

# --- QuizDatabase Class (Handles DB connection and queries) ---
class QuizDatabase:
    def __init__(self, db_name="quiz.db"):
        self.db_path = os.path.join(os.path.dirname(__file__), db_name)
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row # Allows column name access
            self.cursor = self.conn.cursor()
            print(f"Connected to quiz database: {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to quiz database: {e}")
            self.conn = None
            self.cursor = None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Quiz database connection closed.")

    def fetch_categories(self):
        # ... (code as provided previously) ...
        if not self.conn: self.connect()
        if not self.conn: return []
        try:
            self.cursor.execute("SELECT CategoryID, CategoryName FROM Categories ORDER BY CategoryName")
            categories = self.cursor.fetchall()
            return categories
        except sqlite3.Error as e:
            print(f"Error fetching categories: {e}")
            return []

    def fetch_questions_by_category(self, category_id):
        # ... (code as provided previously) ...
        if not self.conn: self.connect()
        if not self.conn: return []
        try:
            query = """
            SELECT
                q.QuestionID,
                q.QuestionText,
                a.AnswerID,
                a.AnswerText,
                a.IsCorrect
            FROM
                Questions q
            JOIN
                Answers a ON q.QuestionID = a.QuestionID
            WHERE
                q.CategoryID = ?
            ORDER BY
                q.QuestionID, a.AnswerID;
            """
            self.cursor.execute(query, (category_id,))
            rows = self.cursor.fetchall()

            questions_data = {}
            for row in rows:
                question_id = row['QuestionID']
                if question_id not in questions_data:
                    questions_data[question_id] = {
                        'question_id': question_id,
                        'question_text': row['QuestionText'],
                        'answers': []
                    }
                questions_data[question_id]['answers'].append({
                    'answer_id': row['AnswerID'],
                    'answer_text': row['AnswerText'],
                    'is_correct': bool(row['IsCorrect'])
                })
            return list(questions_data.values())
        except sqlite3.Error as e:
            print(f"Error fetching questions: {e}")
            return []

# --- End of QuizDatabase Class ---


class QuizUiForm(QtWidgets.QWidget):
    quiz_finished_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        print("QuizUiForm: Initializing...")
        self.setMinimumSize(620, 650)

        self.ui = QuizUi_MainWindow_Generated()
        temp_quiz_window = QtWidgets.QMainWindow()
        try:
            self.ui.setupUi(temp_quiz_window)
        except Exception as e:
            print(f"QuizUiForm: Error during setupUi on temporary QMainWindow: {e}")
            layout = QtWidgets.QVBoxLayout(self)
            layout.addWidget(QtWidgets.QLabel("Error loading quiz UI. Check console for details."))
            self.setLayout(layout)
            return

        quiz_content_widget = temp_quiz_window.centralWidget()
        if quiz_content_widget:
            quiz_content_widget.setParent(self)
            layout = QtWidgets.QVBoxLayout(self)
            layout.addWidget(quiz_content_widget)
            layout.setContentsMargins(0, 0, 0, 0)
            self.setLayout(layout)
        temp_quiz_window.deleteLater()

        # --- Database Initialization (The link!) ---
        self.db = QuizDatabase()
        self.db.connect() # Attempt to connect to quiz.db

        if not self.db.conn:
            QMessageBox.critical(self, "Database Error", "Failed to connect to Quiz Database! Quiz functionality may be limited.")

        # --- Quiz State Variables ---
        self.current_questions = []
        self.current_question_index = -1
        self.correct_answers_count = 0
        self.total_questions_to_ask = 0

        # --- Get References to UI Elements ---
        self.categoryComboBox = self.ui.comboBox_6
        self.numQuestionsSpinBox = self.ui.spinBox_2
        self.getNewQuestionButton = self.ui.pushButton_4
        self.questionTextEdit = self.ui.plainTextEdit
        self.questionCountLabel = self.ui.question_count_label
        self.answer_radio_buttons = [
            self.ui.radioButton, self.ui.radioButton_3, self.ui.radioButton_4, self.ui.radioButton_2
        ]
        self.tryAgainButton = self.ui.pushButton
        self.checkButton = self.ui.pushButton_2
        self.nextButton = self.ui.pushButton_3

        # --- Connect Signals to Slots ---
        self.categoryComboBox.currentIndexChanged.connect(self.category_selected)
        self.getNewQuestionButton.clicked.connect(self.start_quiz_from_settings)
        self.tryAgainButton.clicked.connect(self.try_again)
        self.checkButton.clicked.connect(self.check_answer)
        self.nextButton.clicked.connect(self.next_question)

        # --- Initial UI States ---
        self.nextButton.setEnabled(False)
        self.tryAgainButton.setEnabled(False)
        self.checkButton.setEnabled(False)
        self.questionTextEdit.setReadOnly(True)
        self.clear_answers()

        # Load categories into dropdown on startup (uses DB)
        self.load_categories_into_dropdown()

        if hasattr(self.ui, 'toolBox'):
            self.ui.toolBox.setCurrentIndex(0)
        else:
            print("QuizUiForm: Warning: QToolBox not found in quiz_ui.py. Internal page navigation may not work.")
        print("QuizUiForm: Initialized and UI setup completed.")

    def load_categories_into_dropdown(self):
        """Loads categories from DB into the QComboBox."""
        categories = self.db.fetch_categories() # <--- Uses DB
        self.categoryComboBox.clear()
        self.categoryComboBox.addItem("Select a Category", None)
        if categories:
            for row in categories:
                self.categoryComboBox.addItem(row['CategoryName'], row['CategoryID'])
        else:
            print("No categories found in quiz database.")

    def category_selected(self, index):
        pass

    def start_quiz_from_settings(self):
        selected_category_id = self.categoryComboBox.currentData()
        if selected_category_id is None:
            QMessageBox.warning(self, "No Category Selected", "Please select a quiz category first!")
            return

        self.total_questions_to_ask = self.numQuestionsSpinBox.value()

        all_questions_for_category = self.db.fetch_questions_by_category(selected_category_id) # <--- Uses DB

        if not all_questions_for_category:
            QMessageBox.information(self, "No Questions", "No questions found for the selected category.")
            return

        random.shuffle(all_questions_for_category)
        self.current_questions = all_questions_for_category[:self.total_questions_to_ask]

        if self.current_questions:
            self.current_question_index = 0
            self.correct_answers_count = 0
            self.display_question()
            self.nextButton.setEnabled(False)
            self.checkButton.setEnabled(True)
            self.tryAgainButton.setEnabled(False)
            if hasattr(self.ui, 'toolBox'):
                self.ui.toolBox.setCurrentIndex(1)
        else:
            QMessageBox.information(self, "No Questions", "No questions to display for the selected criteria.")
            self.clear_answers()
            self.nextButton.setEnabled(False)
            self.checkButton.setEnabled(False)
            self.tryAgainButton.setEnabled(False)

    def display_question(self):
        # ... (code as provided previously) ...
        if not self.current_questions or self.current_question_index == -1:
            self.questionTextEdit.setPlainText("No question to display.")
            self.clear_answers()
            return
        question_data = self.current_questions[self.current_question_index]
        question_number_display = self.current_question_index + 1
        total_questions_display = len(self.current_questions)

        self.questionTextEdit.setPlainText(f"Q{question_number_display}/{total_questions_display}: {question_data['question_text']}")
        self.questionCountLabel.setText(f"{question_number_display}/{total_questions_display}")

        for radio_btn in self.answer_radio_buttons:
            radio_btn.setChecked(False)
            radio_btn.setText("")
            radio_btn.setStyleSheet("")
            radio_btn.setEnabled(True)

        shuffled_answers = list(question_data['answers'])
        random.shuffle(shuffled_answers)

        for i, answer in enumerate(shuffled_answers):
            if i < len(self.answer_radio_buttons):
                self.answer_radio_buttons[i].setText(answer['answer_text'])
                self.answer_radio_buttons[i].setProperty("is_correct", answer['is_correct'])
            else:
                print(f"Warning: Question {question_data['question_id']} has more than 4 answers. Only first 4 displayed.")
        self.nextButton.setEnabled(False)
        self.tryAgainButton.setEnabled(False)
        self.checkButton.setEnabled(True)

    def clear_answers(self):
        # ... (code as provided previously) ...
        for radio_btn in self.answer_radio_buttons:
            radio_btn.setText("")
            radio_btn.setChecked(False)
            radio_btn.setStyleSheet("")
            radio_btn.setEnabled(False)

    def check_answer(self):
        # ... (code as provided previously) ...
        selected_button = None
        for radio_btn in self.answer_radio_buttons:
            if radio_btn.isChecked():
                selected_button = radio_btn
                break
        if selected_button is None:
            QMessageBox.information(self, "No Answer Selected", "Please select an answer before checking!")
            return
        for radio_btn in self.answer_radio_buttons:
            radio_btn.setEnabled(False)
        is_correct = selected_button.property("is_correct")
        if is_correct:
            selected_button.setStyleSheet("QRadioButton { color: green; font-weight: bold; }")
            self.correct_answers_count += 1
        else:
            selected_button.setStyleSheet("QRadioButton { color: red; font-weight: bold; }")
            for radio_btn in self.answer_radio_buttons:
                if radio_btn.property("is_correct"):
                    radio_btn.setStyleSheet("QRadioButton { color: green; font-weight: bold; }")
                    break
            self.tryAgainButton.setEnabled(True)
        self.checkButton.setEnabled(False)
        self.nextButton.setEnabled(True)

    def try_again(self):
        # ... (code as provided previously) ...
        for radio_btn in self.answer_radio_buttons:
            radio_btn.setStyleSheet("")
            radio_btn.setEnabled(True)
            radio_btn.setChecked(False)
        self.tryAgainButton.setEnabled(False)
        self.nextButton.setEnabled(False)
        self.checkButton.setEnabled(True)

    def next_question(self):
        # ... (code as provided previously) ...
        self.current_question_index += 1
        if self.current_question_index < len(self.current_questions):
            self.display_question()
        else:
            final_score_message = f"Quiz Finished! You got {self.correct_answers_count} out of {len(self.current_questions)} correct."
            self.questionTextEdit.setPlainText(final_score_message)
            self.clear_answers()
            self.nextButton.setEnabled(False)
            self.checkButton.setEnabled(False)
            self.tryAgainButton.setEnabled(False)

            QMessageBox.information(self, "Quiz Complete", final_score_message)

            self.current_questions = []
            self.current_question_index = -1
            self.correct_answers_count = 0
            self.total_questions_to_ask = 0
            if hasattr(self.ui, 'toolBox'):
                self.ui.toolBox.setCurrentIndex(0)
            self.quiz_finished_signal.emit()

    def closeEvent(self, event):
        """Ensures the database connection is closed when the app exits."""
        if self.db:
            self.db.close()
        super().closeEvent(event)