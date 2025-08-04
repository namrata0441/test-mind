import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QFile, QTextStream # Removed 'Qt' as it's not explicitly used by its direct name (like Qt.AlignCenter)
from sidebar_ui import Ui_MainWindow
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Initial Setup ---
        # Initialize sidebar visibility. Adjust based on your preference:
        self.ui.icon_only_widget.setVisible(True)
        self.ui.full_mwnu_widget.setHidden(True)

        self.ui.stackedWidget.setCurrentIndex(0) # Set initial page to Home Page (index 0)
        self.ui.home_btn_1.setChecked(True) # Set home button (icon-only) as initially checked
        self.ui.home_btn_2.setChecked(True) # Set home button (full menu) as initially checked

        # --- Connect Sidebar Buttons to Stacked Widget Pages ---
        # Home Page (Index 0)
        self.ui.home_btn_1.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(0) if checked else None)
        self.ui.home_btn_2.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(0) if checked else None)

        # Flashcard Page (Index 2 in sidebar_ui.py)
        self.ui.flash_btn_1.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(2) if checked else None)
        self.ui.flash_btn_2.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(2) if checked else None)

        # Quizzes Page (Index 3 in sidebar_ui.py) - Corrected typo "Quizzze"
        self.ui.quizze_btn_1.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(3) if checked else None)
        self.ui.quizze_btn_2.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(3) if checked else None)

        # About Us Page (Index 4 in sidebar_ui.py)
        self.ui.about_btn_1.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(4) if checked else None)
        self.ui.about_btn_2.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(4) if checked else None)

        # Settings Page (Index 5 in sidebar_ui.py)
        self.ui.setting_1.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(5) if checked else None)
        self.ui.setting_2.toggled.connect(lambda checked: self.ui.stackedWidget.setCurrentIndex(5) if checked else None)

        # --- Connect Header Buttons ---
        # Profile Page (Index 1 in sidebar_ui.py) - connected to user_btn
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)

        # Search Page (Index 6 in sidebar_ui.py) - connected to search_btn
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)

        # --- Connect stackedWidget's currentChanged signal to manage button checked state ---
        self.ui.stackedWidget.currentChanged.connect(self.on_stacked_widget_current_changed)


    # --- Function for searching (connected to search_btn) ---
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6) # The search page is at index 6
        search_text = self.ui.search_input.text().strip()

        if search_text:
            self.ui.label_9.setText(f"Search Results for: \"{search_text}\"") # Assuming label_9 is on the search page
        else:
            self.ui.label_9.setText("Please enter text to search.")
            print("Search input is empty.")

    # --- Function for changing page to user page (connected to user_btn) ---
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1) # The profile page is at index 1

    # --- Function to manage QPushButton Checkable status when stackedWidget index changed ---
    # Renamed to lowercase snake_case as per linter suggestion
    def on_stacked_widget_current_changed(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) + \
                   self.ui.full_mwnu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if btn.property("page_index") is not None:
                if btn.property("page_index") == index:
                    btn.setChecked(True)
                    btn.setAutoExclusive(False) # Temporarily disable autoExclusive
                else:
                    btn.setChecked(False)
                    btn.setAutoExclusive(True) # Re-enable autoExclusive
            else:
                if btn != self.ui.home_btn_1 and btn != self.ui.home_btn_2:
                    btn.setAutoExclusive(True)


# --- Main application execution block ---
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # --- Loading style file (style.qss) using QFile and QTextStream ---
    qss_file_path = os.path.join(os.path.dirname(__file__), "style.qss")

    style_file = QFile(qss_file_path)
    if style_file.open(QFile.ReadOnly | QFile.Text):
        style_stream = QTextStream(style_file)
        style_str = style_stream.readAll()
        app.setStyleSheet(style_str)
        style_file.close()
    else:
        print(f"Error: Could not open style.qss at {qss_file_path}. Applying default QSS or no QSS.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())