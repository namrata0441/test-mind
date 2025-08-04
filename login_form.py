import sys
from PyQt5 import QtWidgets, QtCore # Import QtCore for pyqtSignal

# Assuming login_ui.py is the generated UI for this specific form
from login_ui import Ui_Form as Ui_LoginForm # Use Ui_Form from login_ui.py

class LoginUi_Form(QtWidgets.QWidget):
    # Define signals for communication with MainWindow
    login_successful_signal = QtCore.pyqtSignal(str, str) # Emits username and password on login attempt
    switch_to_register_signal = QtCore.pyqtSignal() # Emits when user wants to register

    def __init__(self): # Added __init__ method for proper initialization
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

        # --- Corrected: Connect login button using its actual objectName 'pushButton' ---
        # This button has the text "L o g I n" in your login.ui
        if hasattr(self.ui, 'pushButton'):
            self.ui.pushButton.clicked.connect(self._emit_login_signal)
            print("Debug: 'pushButton' (Login) connected.")
        else:
            print("Warning: 'pushButton' for login not found in LoginUi_Form. Login button might not work.")

        # --- Corrected: Connect register button/link using its actual objectName 'forgotPasswordLabel_2' ---
        # This button has the text "Forgot your UserName or Password?|Sign Up" in your login.ui
        # It's a QPushButton, so its clicked signal can be used for navigation.
        if hasattr(self.ui, 'forgotPasswordLabel_2') and isinstance(self.ui.forgotPasswordLabel_2, QtWidgets.QPushButton):
            # Added a lambda function to include a debug print statement
            self.ui.forgotPasswordLabel_2.clicked.connect(lambda: (print("Debug: 'forgotPasswordLabel_2' (Switch to Register) clicked. Emitting signal."), self.switch_to_register_signal.emit()))
            print("Debug: 'forgotPasswordLabel_2' (Register link) connected.")
        else:
            print("Warning: 'forgotPasswordLabel_2' (Register button) not found or not QPushButton in LoginUi_Form.")

        # --- Corrected: Access LineEdits using their actual objectNames 'lineEdit' and 'lineEdit_2' ---
        self.username_input = self.ui.lineEdit if hasattr(self.ui, 'lineEdit') else None
        self.password_input = self.ui.lineEdit_2 if hasattr(self.ui, 'lineEdit_2') else None

        if self.username_input:
            self.username_input.setPlaceholderText("Enter User Name") # Matched placeholder from your UI
        if self.password_input:
            self.password_input.setPlaceholderText("Enter Password") # Matched placeholder from your UI
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password) # Ensure password echo mode is set
        else:
            print("Warning: 'lineEdit_2' (password input) not found in LoginUi_Form. Password echo mode not set.")


    def _emit_login_signal(self):
        # This method will collect data and emit the signal for MainWindow to handle login via backend
        username = self.username_input.text().strip() if self.username_input else ""
        password = self.password_input.text().strip() if self.password_input else ""
        print(f"Debug: Login signal emitted from _emit_login_signal for user: {username}")
        self.login_successful_signal.emit(username, password) # Emit username and password

    def clear_fields(self):
        """Clears the username and password input fields."""
        if self.username_input:
            self.username_input.clear()
        if self.password_input:
            self.password_input.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_form = LoginUi_Form()
    login_form.show()
    sys.exit(app.exec_())
