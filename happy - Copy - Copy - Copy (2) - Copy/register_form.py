import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests  # CRITICAL: Import requests for backend communication
import res_rc  # This imports your compiled resources

class RegisterUi_Form(QtWidgets.QWidget):  # Class for the registration form
    # Define signals for communication with the main application
    registration_successful_signal = QtCore.pyqtSignal()
    switch_to_login_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        # CRITICAL FIX: Call setupUi here to initialize the UI elements
        self.setupUi(self)

        # Initialize instance attributes to None or default values (these are now set by setupUi)
        # However, it's good practice to ensure they are accessible as instance variables
        self.widget = self.findChild(QtWidgets.QWidget, "widget")
        self.label_3 = self.findChild(QtWidgets.QLabel, "label_3")  # Background label

        # Access LineEdits by their objectNames from the UI
        self.lineEdit_full_name = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.lineEdit_phone_number = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, "lineEdit_6")  # Corrected objectName for password
        self.lineEdit_email = self.findChild(QtWidgets.QLineEdit, "lineEdit_4")
        self.lineEdit_country = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")  # Corrected objectName for country
        self.lineEdit_confirm_password = self.findChild(QtWidgets.QLineEdit, "lineEdit_5")

        # Access Buttons by their objectNames from the UI
        self.register_button = self.findChild(QtWidgets.QPushButton,
                                              "pushButton")  # Corrected objectName for Register Now! button
        self.already_have_account_button = self.findChild(QtWidgets.QPushButton,
                                                          "forgotPasswordLabel")  # Corrected objectName for Already have an account? button

        # Connect signals and slots
        if self.register_button:
            self.register_button.clicked.connect(self.register_user)
        if self.already_have_account_button:
            self.already_have_account_button.clicked.connect(self.switch_to_login_signal.emit)

        # Set password echo modes
        if self.lineEdit_password:
            # Corrected syntax for accessing Password echo mode
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.lineEdit_confirm_password:
            # Corrected syntax for accessing Password echo mode
            self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, Form):
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
        self.pushButton = QtWidgets.QPushButton(self.widget)  # This is your "Register Now!" button
        self.pushButton.setGeometry(QtCore.QRect(270, 430, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")  # Changed objectName to "pushButton" as per your UI
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(160, 20, 51, 41))
        self.label.setStyleSheet("background-image: url(:/image/Users/DELL/Desktop/MindZap/mz.jpg);")
        self.label.setText("")
        # CRITICAL FIX: Use correct resource path
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
        # CRITICAL FIX: Use correct resource path
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
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)  # Corrected syntax
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
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)  # Corrected syntax
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.forgotPasswordLabel = QtWidgets.QPushButton(self.widget)  # This is your "Already have an account?" button
        self.forgotPasswordLabel.setGeometry(QtCore.QRect(310, 510, 211, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        self.forgotPasswordLabel.setFont(font)
        self.forgotPasswordLabel.setObjectName("forgotPasswordLabel")  # Corrected objectName as per your UI

        # The widget_2 block seems to be a duplicate of the main widget's content
        # It's usually better to have one main form.
        # For now, I'm assuming the primary inputs are the ones directly under 'widget'
        # and not the ones under 'widget_2'. If your UI uses widget_2 for the actual inputs,
        # you'll need to adjust the findChild calls in __init__ to target widget_2's elements.
        # For example: self.lineEdit_full_name = self.findChild(QtWidgets.QLineEdit, "lineEdit_7")

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

    def register_user(self):
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

        # --- Send data to Flask Backend ---
        backend_url = "http://127.0.0.1:5000/register"
        registration_data = {
            "username": email,  # Using email as username for backend
            "password": password,
            "full_name": full_name,
            "phone_number": phone_number,
            "email": email,
            "country": country
        }

        print(f"Frontend Debug: Sending data to backend: {registration_data}") # Debug: See what's being sent

        try:
            response = requests.post(backend_url, json=registration_data)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

            print(f"Frontend Debug: Raw response text from backend: {response.text}") # Debug: See raw response

            # This is the line that likely causes the "Expecting value" error if response.text is not valid JSON
            response_data = response.json()

            if response.status_code == 201:  # HTTP 201 Created for successful registration
                QtWidgets.QMessageBox.information(self, "Registration Success",
                                                  response_data.get("message", "User registered successfully!"))
                self.clear_fields()
                self.registration_successful_signal.emit()  # Emit signal to main app
            elif response.status_code == 409:  # HTTP 409 Conflict (e.g., email already taken)
                QtWidgets.QMessageBox.warning(self, "Registration Failed", response_data.get("message",
                                                                                             "Email already registered or username taken."))
            else:
                # Catch any other unexpected successful status codes but with an error message
                QtWidgets.QMessageBox.warning(self, "Registration Failed", response_data.get("message",
                                                                                             "An unknown error occurred during registration."))

        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error",
                                           "Could not connect to the backend server. Please ensure Flask app is running.")
        except requests.exceptions.HTTPError as e:
            # This catches 4xx or 5xx errors where the server returned a non-2xx status
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                # Try to parse JSON from error response if available
                error_json = e.response.json()
                error_message += f" - {error_json.get('message', e.response.text)}"
            except requests.exceptions.JSONDecodeError:
                error_message += f" - {e.response.text}" # Fallback to raw text if not JSON
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
        except requests.exceptions.JSONDecodeError as e:
            # THIS IS THE CRITICAL CATCH FOR "Expecting value line 1 column 1 (char 0)"
            QtWidgets.QMessageBox.critical(self, "Response Error",
                                           f"Failed to parse server response as JSON. This usually means the backend did not send valid JSON. Error: {e}. Raw Response: '{response.text}'")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred during registration: {e}")

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
