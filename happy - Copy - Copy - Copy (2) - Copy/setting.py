from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal # Import pyqtSignal
import json
import os
import requests # Import requests for API calls

SETTINGS_FILE = "settings.json" # Define the file name for saving settings

class SettingsWidget(QWidget):
    # New signal to emit when settings (email/password) are successfully updated
    settings_updated_signal = pyqtSignal(str) # Emits the new email (username)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout() # Main layout for the widget

        self.current_user_email = None # To store the email of the currently logged-in user

        # Email input field
        self.email_input = QLineEdit() # Renamed from username_input to email_input
        self.email_input.setPlaceholderText("Enter new email") # Updated placeholder text

        # Password input field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter new password")
        self.password_input.setEchoMode(QLineEdit.Password) # Hide password characters

        # Dark mode checkbox
        self.dark_mode_checkbox = QCheckBox("Enable Dark Mode")
        # Connect the stateChanged signal to the toggle_dark_mode method
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)

        # Save button
        save_button = QPushButton("Save Changes") # Changed button text for clarity
        # Connect the clicked signal to the save_settings method
        save_button.clicked.connect(self.save_settings)

        # Add widgets to the layout
        self.layout.addWidget(QLabel("Change Email:")) # Updated label text
        self.layout.addWidget(self.email_input) # Updated to email_input
        self.layout.addWidget(QLabel("Change Password:"))
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.dark_mode_checkbox)
        self.layout.addWidget(save_button)
        self.layout.addStretch() # Add a stretch to push content to the top

        self.setLayout(self.layout) # Set the layout for the widget

        self.load_settings() # Load existing settings when the widget is initialized

    def set_current_user_email(self, email):
        """Sets the current user's email, typically called by the main app."""
        self.current_user_email = email
        # Optionally, you might want to pre-fill the email_input with the current email
        # self.email_input.setText(email) # Decide if you want to show current email here

    def load_settings(self):
        """Loads settings from the SETTINGS_FILE and updates the UI."""
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    data = json.load(f)
                    # Set the dark mode checkbox based on loaded data
                    self.dark_mode_checkbox.setChecked(data.get("dark_mode", False))
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Settings Error", "Could not read settings file. It might be corrupted.")
            except Exception as e:
                QMessageBox.warning(self, "Settings Error", f"An error occurred loading settings: {e}")

    def toggle_dark_mode(self, state):
        """
        Toggles dark mode setting and saves it to a file.
        Note: Actual theme application would require more complex logic
        and likely a restart or dynamic stylesheet changes in the main app.
        """
        dark_mode = state == Qt.Checked
        try:
            with open(SETTINGS_FILE, "w") as f:
                json.dump({"dark_mode": dark_mode}, f, indent=4)
            QMessageBox.information(self, "Theme Changed", "Theme setting saved. Please restart the app to apply the new theme.")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Failed to save theme setting: {e}")

    def save_settings(self):
        """
        Collects data from fields and sends it to the backend for update.
        This will update both email and password.
        """
        if not self.current_user_email:
            QMessageBox.warning(self, "Error", "No current user email available for update. Please log in.")
            return

        new_email = self.email_input.text().strip()
        new_password = self.password_input.text().strip()

        # If neither email nor password is provided, there's nothing to update
        if not new_email and not new_password:
            QMessageBox.information(self, "No Changes", "No new email or password entered.")
            return

        # Prepare data for backend
        update_data = {
            "current_username": self.current_user_email, # Send current email as username
            "new_username": new_email if new_email else self.current_user_email, # Use new_email if provided, else keep current
            "new_password": new_password # Send new password (even if empty, backend should handle)
        }

        backend_url = "http://127.0.0.1:5000/update_credentials"
        print(f"Frontend Debug (Settings): Sending update data: {update_data}")

        response = None # Initialize response to None to prevent "might be referenced before assignment" error
        try:
            response = requests.post(backend_url, json=update_data)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            response_data = response.json()

            if response.status_code == 200:
                QMessageBox.information(self, "Settings Saved", response_data.get("message", "Settings updated successfully!"))
                # If email was changed, update the current_user_email and emit signal
                if new_email and new_email != self.current_user_email:
                    self.current_user_email = new_email
                    self.settings_updated_signal.emit(new_email) # Emit new email
                else:
                    # If only password changed or no email change, still emit current email
                    self.settings_updated_signal.emit(self.current_user_email)
                self.email_input.clear()
                self.password_input.clear()
            else:
                QMessageBox.warning(self, "Update Failed", response_data.get("message", "Failed to update settings."))

        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Connection Error", "Could not connect to the backend server. Please ensure Flask app is running.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                # Ensure response is not None before trying to parse JSON
                if response: # Check if response object exists before accessing it
                    error_json = response.json()
                    error_message += f" - {error_json.get('message', response.text)}"
                else:
                    error_message += f" - No response received."
            except requests.exceptions.JSONDecodeError:
                if response: # Check if response object exists before accessing it
                    error_message += f" - {response.text}"
                else:
                    error_message += f" - No response received."
            QMessageBox.critical(self, "Server Error", error_message)
        except requests.exceptions.JSONDecodeError as e:
            QMessageBox.critical(self, "Response Error", f"Failed to parse server response as JSON. Error: {e}. Raw Response: '{response.text if response else 'No response'}'")
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred during settings update: {e}")

# This part allows you to run the SettingsWidget independently for testing
if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets # Import QtWidgets for the standalone execution block
    app = QtWidgets.QApplication(sys.argv)
    settings_widget = SettingsWidget()
    settings_widget.show()
    sys.exit(app.exec_())
