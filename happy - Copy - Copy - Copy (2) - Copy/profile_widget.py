import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class ProfileWidget(QtWidgets.QWidget):
    # Signals for communication with the main application
    logout_requested = QtCore.pyqtSignal()
    profile_updated = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.edit_mode = False # Flag to track edit mode

        self._setup_ui() # Call a helper method to set up the UI
        self._init_connections() # Set up button connections
        self.set_fields_read_only(True) # Start in read-only mode

        self.setWindowTitle("MindZap - User Profile") # Set window title if this widget were standalone

    def _setup_ui(self):
        """Programmatically sets up the UI elements for the profile."""
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Title
        title_label = QtWidgets.QLabel("<h2>User Profile</h2>")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Profile Picture (Placeholder)
        profile_pic_label = QtWidgets.QLabel()
        # Ensure you have a resource file (res_rc.py) that includes this icon
        # If not, you might need to adjust the path or add it to your .qrc file.
        profile_pic_label.setPixmap(QtGui.QPixmap(":/icon/icon/person_icon.png").scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        profile_pic_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(profile_pic_label)

        # Form Layout for fields
        form_layout = QtWidgets.QFormLayout()
        form_layout.setContentsMargins(50, 20, 50, 20)
        form_layout.setVerticalSpacing(15)

        # Full Name
        self.full_name_input = QtWidgets.QLineEdit()
        self.full_name_input.setPlaceholderText("Full Name")
        form_layout.addRow("Full Name:", self.full_name_input)

        # Phone Number
        self.phone_number_input = QtWidgets.QLineEdit()
        self.phone_number_input.setPlaceholderText("Phone Number")
        form_layout.addRow("Phone Number:", self.phone_number_input)

        # Email (Username) - typically read-only
        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setReadOnly(True) # Email should generally not be editable via profile
        form_layout.addRow("Email:", self.email_input)

        # Country
        self.country_input = QtWidgets.QLineEdit()
        self.country_input.setPlaceholderText("Country")
        form_layout.addRow("Country:", self.country_input)

        main_layout.addLayout(form_layout)

        # Buttons Layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()

        self.edit_button = QtWidgets.QPushButton("Edit")
        self.edit_button.setFixedSize(100, 30)
        self.edit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green */
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        button_layout.addWidget(self.edit_button)

        self.logout_button = QtWidgets.QPushButton("Logout")
        self.logout_button.setFixedSize(100, 30)
        self.logout_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; /* Red */
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:pressed {
                background-color: #b71c1c;
            }
        """)
        button_layout.addWidget(self.logout_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)
        main_layout.addStretch() # Push content to top

    def _init_connections(self):
        """Connects signals to slots for the profile widget."""
        self.edit_button.clicked.connect(self.toggle_edit_mode)
        self.logout_button.clicked.connect(self.logout_requested.emit)

    def set_fields_read_only(self, read_only):
        """Sets the read-only state for editable input fields."""
        self.full_name_input.setReadOnly(read_only)
        self.phone_number_input.setReadOnly(read_only)
        # self.email_input is always read-only
        self.country_input.setReadOnly(read_only)

    def load_profile_data(self, data):
        """
        Loads profile data received from the backend into the UI fields.
        :param data: A dictionary containing user profile information.
        """
        print(f"Debug ProfileWidget: Loading data: {data}")
        self.full_name_input.setText(data.get('full_name', ''))
        self.phone_number_input.setText(data.get('phone_number', ''))
        self.email_input.setText(data.get('username', '')) # Use 'username' from backend as email
        self.country_input.setText(data.get('country', ''))
        print("Debug ProfileWidget: Fields populated.")

    def toggle_edit_mode(self):
        """Toggles between read-only and editable mode."""
        self.edit_mode = not self.edit_mode
        self.set_fields_read_only(not self.edit_mode) # If edit_mode is True, set read_only to False

        if self.edit_mode:
            self.edit_button.setText("Save")
            QtWidgets.QMessageBox.information(self, "Edit Mode", "You can now edit your profile. Click 'Save' when done.")
        else:
            self.edit_button.setText("Edit")
            self.save_profile_changes() # Save changes when exiting edit mode
        print(f"Debug: Edit mode toggled to: {self.edit_mode}")

    def save_profile_changes(self):
        """
        Collects data from fields and sends it to the backend for update.
        """
        updated_data = {
            'full_name': self.full_name_input.text().strip(),
            'phone_number': self.phone_number_input.text().strip(),
            'username': self.email_input.text().strip(), # Send email as 'username' to backend
            'country': self.country_input.text().strip()
        }
        print(f"Debug: Attempting to save profile changes: {updated_data}")

        # --- Send updated data to Flask Backend ---
        backend_url = "http://127.0.0.1:5000/profile/update"
        response = None
        try:
            response = requests.post(backend_url, json=updated_data)
            response.raise_for_status()
            response_data = response.json()
            if response_data.get("status") == "success":
                QtWidgets.QMessageBox.information(self, "Profile Update", response_data.get("message", "Profile updated successfully!"))
                self.profile_updated.emit(updated_data) # Emit signal with updated data
            else:
                QtWidgets.QMessageBox.warning(self, "Profile Update Failed", response_data.get("message", "Failed to update profile."))
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error", "Could not connect to backend to update profile.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                if response:
                    error_json = response.json()
                    error_message += f" - {error_json.get('message', response.text)}"
                else:
                    error_message += f" - No response received."
            except requests.exceptions.JSONDecodeError:
                if response:
                    error_message += f" - {response.text}"
                else:
                    error_message += f" - No response received."
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
        except requests.exceptions.JSONDecodeError as e:
            QtWidgets.QMessageBox.critical(self, "Response Error",
                                           f"Failed to parse server response as JSON. Error: {e}. Raw Response: '{response.text if response else 'No response'}'")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred during profile update: {e}")

    def clear_fields(self):
        """Clears all input fields on the form."""
        self.full_name_input.clear()
        self.phone_number_input.clear()
        self.email_input.clear()
        self.country_input.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    profile_widget = ProfileWidget()
    # Dummy data for testing
    dummy_data = {
        'full_name': 'John Doe',
        'phone_number': '123-456-7890',
        'username': 'john.doe@example.com', # Backend uses 'username' for email
        'country': 'USA'
    }
    profile_widget.load_profile_data(dummy_data)
    profile_widget.show()
    sys.exit(app.exec_())
