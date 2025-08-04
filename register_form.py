# --- registration_form.py (Corrected for Separation of Concerns) ---
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests  # This import is no longer needed here, but kept for clarity
import res_rc  # This imports your compiled resources

class RegisterUi_Form(QtWidgets.QWidget):  # Class for the registration form
    # Redefine the signal to pass the registration data as a dictionary
    registration_attempt_signal = QtCore.pyqtSignal(dict)
    switch_to_login_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize instance attributes to None or default values
        self.widget = self.findChild(QtWidgets.QWidget, "widget")
        self.label_3 = self.findChild(QtWidgets.QLabel, "label_3")

        # Access LineEdits by their objectNames from the UI
        self.lineEdit_full_name = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.lineEdit_phone_number = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, "lineEdit_6")
        self.lineEdit_email = self.findChild(QtWidgets.QLineEdit, "lineEdit_4")
        self.lineEdit_country = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        self.lineEdit_confirm_password = self.findChild(QtWidgets.QLineEdit, "lineEdit_5")

        # Access Buttons by their objectNames from the UI
        self.register_button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.already_have_account_button = self.findChild(QtWidgets.QPushButton, "forgotPasswordLabel")

        # Connect signals and slots
        if self.register_button:
            # Connect the button to the new method that collects and emits data
            self.register_button.clicked.connect(self.collect_and_emit_data)
        if self.already_have_account_button:
            self.already_have_account_button.clicked.connect(self.switch_to_login_signal.emit)

        # Set password echo modes
        if self.lineEdit_password:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.lineEdit_confirm_password:
            self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, Form):
        # ... (setup code remains the same) ...
        Form.setObjectName("Form")
        Form.resize(749, 650)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 691, 631))
        self.widget.setStyleSheet("/* Styling for the Register Button */\n"
                                  "QPushButton#registerButton {\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                  "    color: rgba(255, 255, 255, 210);\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#registerButton:hover {\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#registerButton:pressed {\n"
                                  "    padding-left: 5px;\n"
                                  "    padding-top: 5px;\n"
                                  "    background-color: rgba(150, 123, 111, 255);\n"
                                  "}\n"
                                  "\n"
                                  "/* Styling for the \"Already have an account?\" button */\n"
                                  "QPushButton#alreadyAccountButton {\n"
                                  "    background-color: transparent;\n"
                                  "    color: #007bff; /* A blue color for links */\n"
                                  "    border: none;\n"
                                  "    text-decoration: underline;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#alreadyAccountButton:hover {\n"
                                  "    color: #0056b3;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#alreadyAccountButton:pressed {\n"
                                  "    padding-left: 2px;\n"
                                  "    padding-top: 2px;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 561, 611))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(211, 211, 211, 255);\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 200, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border: none;\n"
                                    "border-bottom:2px solid rgba(46,82,101,200);\n"
                                    "color:rgba(0,0,0,240);\n"
                                    "padding-bottom:7px;\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 260, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border: none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(270, 430, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(160, 20, 51, 41))
        self.label.setStyleSheet("background-image: url(:/image/Users/DELL/Desktop/MindZap/mz.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/mz.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 161, 151))
        self.label_2.setStyleSheet("\n"
                                   "background-color: rgba(180, 52, 85, 255);\n"
                                   "\n"
                                   "")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/image/profile.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 200, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border: none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;\n"
                                      "")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 260, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border: none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;\n"
                                      "")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 320, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border: none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;\n"
                                      "")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 320, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border: none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;\n"
                                      "")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.forgotPasswordLabel = QtWidgets.QPushButton(self.widget)
        self.forgotPasswordLabel.setGeometry(QtCore.QRect(310, 510, 211, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        self.forgotPasswordLabel.setFont(font)
        self.forgotPasswordLabel.setObjectName("forgotPasswordLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Register"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Full Name:"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Phone Number:"))
        self.pushButton.setText(_translate("Form", "Register Now!"))
        self.label.setWhatsThis(_translate("Form",
                                           "<html><head/><body><p><img src=\":/image/Users/DELL/Desktop/MindZap/mz.jpg\"/></p></body></html>"))
        self.label_2.setWhatsThis(_translate("Form",
                                             "<html><head/><body><p><img src=\":/image/Users/DELL/Downloads/profile.jpeg\"/></p></body></html>"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Email:"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Country:"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Confirm Password:"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Password:"))
        self.forgotPasswordLabel.setText(_translate("Form", "Already have an account?"))

    def collect_and_emit_data(self):
        """
        Collects all user input and emits a signal with the data for the
        main application to handle the registration attempt.
        """
        full_name = self.lineEdit_full_name.text() if self.lineEdit_full_name else ""
        phone_number = self.lineEdit_phone_number.text() if self.lineEdit_phone_number else ""
        password = self.lineEdit_password.text() if self.lineEdit_password else ""
        email = self.lineEdit_email.text() if self.lineEdit_email else ""
        country = self.lineEdit_country.text() if self.lineEdit_country else ""
        confirm_password = self.lineEdit_confirm_password.text() if self.lineEdit_confirm_password else ""

        if not all([full_name, phone_number, password, email, country, confirm_password]):
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Please fill in all fields.")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Passwords do not match.")
            return

        # Create a dictionary with the registration data
        registration_data = {
            "username": email,
            "password": password,
            "full_name": full_name,
            "phone_number": phone_number,
            "email": email,
            "country": country
        }

        # Emit the signal with the data
        self.registration_attempt_signal.emit(registration_data)

    def clear_fields(self):
        """Clears all input fields on the form."""
        if self.lineEdit_full_name: self.lineEdit_full_name.clear()
        if self.lineEdit_phone_number: self.lineEdit_phone_number.clear()
        if self.lineEdit_email: self.lineEdit_email.clear()
        if self.lineEdit_country: self.lineEdit_country.clear()
        if self.lineEdit_password: self.lineEdit_password.clear()
        if self.lineEdit_confirm_password: self.lineEdit_confirm_password.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    register_form = RegisterUi_Form()
    register_form.show()
    sys.exit(app.exec_())
