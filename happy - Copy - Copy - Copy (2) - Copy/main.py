import sys
import os # Keep os for potential path handling if needed elsewhere in frontend
from PyQt5 import QtWidgets, QtCore, QtGui
import requests
import webbrowser

# Import your UI forms from their respective files
from login_form import LoginUi_Form
from register_form import RegisterUi_Form
from dashboard_form import Ui_MainWindow # This imports the generated UI setup

# Import custom widgets (these are explicitly imported to allow isinstance checks)
# Make sure these files (e.g., profile_widget.py) exist and define these classes
from profile_widget import ProfileWidget
from aboutUs import AboutUsWidget
from setting import SettingsWidget
from flashcard_page import FlashcardPage
from quiz_form import QuizUiForm

# ----------------------------------------------------------------------
# MainApplicationWindow (Dashboard Window) - Define this first
# This class acts as the actual QMainWindow for the dashboard content.
# ----------------------------------------------------------------------
class MainApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, username: str, user_id: int, coordinator: 'ApplicationCoordinator'): # Use forward reference for coordinator
        super().__init__()
        self.setWindowTitle(f"MindZap Application - Dashboard ({username})")
        self.setGeometry(100, 100, 1024, 768)

        self.current_username = username
        self.current_user_id = user_id
        self.coordinator = coordinator # Reference to the ApplicationCoordinator for logout/app flow

        # Initialize Dashboard UI (Ui_MainWindow) and set it up on THIS QMainWindow
        self.dashboard_ui = Ui_MainWindow()
        self.dashboard_ui.setupUi(self) # Set up the UI on this QMainWindow instance

        # Access the stackedWidget which is now an attribute of self.dashboard_ui
        self.dashboard_content_stacked_widget = self.dashboard_ui.stackedWidget

        # Set the username display label immediately
        self.dashboard_ui.set_username_display(self.current_username)

        self.init_connections()

        # Pass user_id to relevant dashboard pages if they need it
        # Ensure these pages have a set_current_user_id method
        if hasattr(self.dashboard_ui.page_2, 'set_current_user_id') and isinstance(self.dashboard_ui.page_2, FlashcardPage):
            self.dashboard_ui.page_2.set_current_user_id(self.current_user_id)
        if hasattr(self.dashboard_ui.page_3, 'set_current_user_id') and isinstance(self.dashboard_ui.page_3, QuizUiForm):
            self.dashboard_ui.page_3.set_current_user_id(self.current_user_id)
        # Add similar calls for any other pages that need user_id (e.g., page_7 for profile if it needs user_id for updates)

    def init_connections(self):
        """
        Connects signals from the dashboard UI elements to their corresponding slots.
        """
        # Connect sidebar buttons to switch pages within the dashboard's internal stackedWidget
        self.dashboard_ui.home_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(0) if checked else None)
        self.dashboard_ui.home_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(0) if checked else None)

        self.dashboard_ui.flash_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(2) if checked else None) # Assuming FlashcardPage is page_2
        self.dashboard_ui.flash_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(2) if checked else None)

        self.dashboard_ui.quizze_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(3) if checked else None) # Assuming QuizUiForm is page_3
        self.dashboard_ui.quizze_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(3) if checked else None)

        self.dashboard_ui.about_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(4) if checked else None) # Assuming AboutUsWidget is page_4
        self.dashboard_ui.about_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(4) if checked else None)

        # Settings buttons: connect to a method that also passes user email
        self.dashboard_ui.setting_1.toggled.connect(lambda checked: self.show_settings_page() if checked else None) # Assuming SettingsWidget is page_5
        self.dashboard_ui.setting_2.toggled.connect(lambda checked: self.show_settings_page() if checked else None)

        # Profile button: connect to a method that fetches and loads profile data
        self.dashboard_ui.user_btn.clicked.connect(self.show_profile_page) # Assuming ProfileWidget is page_1 or page_7

        # Search functionality: connect from dashboard_ui's widgets
        self.dashboard_ui.search_btn.clicked.connect(self.perform_google_search)
        self.dashboard_ui.search_input.returnPressed.connect(self.perform_google_search)

        # Logout buttons: connect to the coordinator's show_login_page method
        self.dashboard_ui.logout_btn_1.clicked.connect(self.coordinator.show_login_page)
        self.dashboard_ui.logout_btn_2.clicked.connect(self.coordinator.show_login_page)


    def _fetch_profile_data(self, username):
        """Fetches user profile data from the backend."""
        if not username:
            print("Error: No username available to fetch profile.")
            return None

        backend_url = f"http://127.0.0.1:5000/profile/{username}"
        response = None
        try:
            response = requests.get(backend_url, timeout=5) # Added timeout for robustness
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            profile_data = response.json()
            print(f"Frontend Debug (MainApp - Profile Fetch): Fetched profile: {profile_data}")
            return profile_data
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error", "Could not connect to backend to fetch profile. Ensure backend server is running.")
            print("Frontend Debug (MainApp - Profile Fetch): ConnectionError: Backend server unreachable.")
        except requests.exceptions.Timeout:
            QtWidgets.QMessageBox.critical(self, "Connection Timeout", "Backend server took too long to respond.")
            print("Frontend Debug (MainApp - Profile Fetch): Timeout: Backend server did not respond in time.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                if e.response: # Check if response object exists
                    error_json = e.response.json()
                    error_message += f" - {error_json.get('message', e.response.text)}"
                else:
                    error_message += f" - No readable response received."
            except requests.exceptions.JSONDecodeError: # Handle cases where response isn't JSON
                if e.response:
                    error_message += f" - Raw response: {e.response.text}"
                else:
                    error_message += f" - No readable response received."
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
            print(f"Frontend Debug (MainApp - Profile Fetch): HTTP error: {error_message}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred fetching profile: {e}")
            print(f"Frontend Debug (MainApp - Profile Fetch): Unexpected error: {e}")
        return None

    def perform_google_search(self):
        """Performs a Google search based on the input in the search bar."""
        # Ensure 'search_input' is a valid QLineEdit or similar widget in your Ui_MainWindow
        if hasattr(self.dashboard_ui, 'search_input') and isinstance(self.dashboard_ui.search_input, QtWidgets.QLineEdit):
            search_query = self.dashboard_ui.search_input.text().strip()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                print(f"Performed Google search for: {search_query}")
            else:
                QtWidgets.QMessageBox.information(self, "Search", "Please enter a search query.")
            self.dashboard_ui.search_input.clear() # Clear input after search
        else:
            QtWidgets.QMessageBox.warning(self, "Search Error", "Search input widget not found or not a QLineEdit.")
            print("Error: 'search_input' widget not found or not a QLineEdit in dashboard_ui.")

    def show_settings_page(self):
        """
        This method is called when a settings button is clicked on the dashboard.
        It passes the current user's email to the SettingsWidget before displaying it.
        """
        if self.current_username:
            # Ensure your SettingsWidget (page_5) has a method like set_current_user_email
            if hasattr(self.dashboard_ui.page_5, 'set_current_user_email') and isinstance(self.dashboard_ui.page_5, SettingsWidget):
                self.dashboard_ui.page_5.set_current_user_email(self.current_username)
                print(f"Debug MainApp: Passed email '{self.current_username}' to SettingsWidget.")
                self.dashboard_content_stacked_widget.setCurrentIndex(5) # Index 5 is the Settings Page (self.page_5)
                self.setWindowTitle(f"MindZap - Settings ({self.current_username})")
                print(f"Switched to Settings Page for user: {self.current_username}")
            else:
                QtWidgets.QMessageBox.warning(self, "Settings Error", "Settings widget not found or not initialized correctly with 'set_current_user_email' method.")
                print("Error: SettingsWidget (page_5) does not have 'set_current_user_email' method or is not a SettingsWidget instance.")
        else:
            QtWidgets.QMessageBox.warning(self, "Settings Error", "No user logged in to access settings.")
            self.coordinator.show_login_page() # Redirect to login if no user is logged in

    def show_profile_page(self):
        """
        This method is called when the user clicks the profile button on the dashboard.
        It fetches the profile data and loads it into the ProfileWidget.
        """
        if self.current_username:
            profile_data = self._fetch_profile_data(self.current_username)
            if profile_data:
                # Ensure your ProfileWidget (page_7) has a method like load_profile_data
                if hasattr(self.dashboard_ui.page_7, 'load_profile_data') and isinstance(self.dashboard_ui.page_7, ProfileWidget):
                    self.dashboard_ui.page_7.load_profile_data(profile_data)
                    self.dashboard_content_stacked_widget.setCurrentIndex(1) # Index 1 is the Profile Page (self.page_7)
                    self.setWindowTitle(f"MindZap - Profile ({self.current_username})")
                    print(f"Switched to Profile Page for user: {self.current_username}")
                else:
                    QtWidgets.QMessageBox.warning(self, "Profile Error", "Profile widget not found or not initialized correctly with 'load_profile_data' method.")
                    print("Error: ProfileWidget (page_7) does not have 'load_profile_data' method or is not a ProfileWidget instance.")
            else:
                QtWidgets.QMessageBox.warning(self, "Profile Error", "Could not load profile data.")
        else:
            QtWidgets.QMessageBox.warning(self, "Profile Error", "No user logged in to view profile.")
            self.coordinator.show_login_page() # Redirect to login if no user is logged in


# ----------------------------------------------------------------------
# ApplicationCoordinator (Main entry point of the PyQt5 frontend)
# This class manages the top-level windows (Login, Register, Dashboard).
# ----------------------------------------------------------------------
class ApplicationCoordinator(QtWidgets.QMainWindow): # Changed to QMainWindow to be the top-level window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MindZap Application")
        self.setGeometry(100, 100, 800, 600) # Initial size for the coordinator window

        # The main stacked widget for switching between Login/Register/Dashboard
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget) # Set the stacked widget as the central widget

        self.login_page = LoginUi_Form()
        self.register_page = RegisterUi_Form()
        self.dashboard_window = None # Will be an instance of MainApplicationWindow, created on login

        self.current_username = None # To store the username (email) of the logged-in user
        self.current_user_id = None # To store the user_id of the logged-in user

        # Add initial pages to the stacked widget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)

        self.init_coordinator_connections()
        self.show_login_page() # Start with the login page

    def init_coordinator_connections(self):
        """Connections for overall app flow managed by the coordinator."""
        self.login_page.login_successful_signal.connect(self._handle_login_attempt)
        self.login_page.switch_to_register_signal.connect(self.show_register_page)
        self.register_page.registration_successful_signal.connect(self._handle_registration_attempt)
        self.register_page.switch_to_login_signal.connect(self.show_login_page)

    def _handle_login_attempt(self, username, password):
        """
        Handles the login attempt by making a request to the backend.
        This method is connected to login_page.login_successful_signal.
        """
        backend_url = "http://127.0.0.1:5000/login" # Ensure your Flask backend is running on this URL
        login_data = {
            "username": username,
            "password": password
        }

        print(f"Frontend Debug (Coordinator - Login): Sending data to backend: {login_data}")

        response = None
        try:
            response = requests.post(backend_url, json=login_data, timeout=5) # Added timeout
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

            response_data = response.json()
            print(f"Frontend Debug (Coordinator - Login): Received response: {response_data}")

            if response.status_code == 200:
                QtWidgets.QMessageBox.information(self, "Login Success", response_data.get("message", "Login successful!"))
                self.login_page.clear_fields()
                self.current_username = response_data.get("username", username)
                self.current_user_id = response_data.get("user_id") # Get user_id from backend response
                self.show_dashboard_page(self.current_username, self.current_user_id)
            else:
                QtWidgets.QMessageBox.warning(self, "Login Failed", response_data.get("message", "Invalid credentials."))

        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error",
                                           "Could not connect to the backend server. Please ensure Flask app is running.")
            print("Frontend Debug (Coordinator - Login): ConnectionError: Backend server unreachable.")
        except requests.exceptions.Timeout:
            QtWidgets.QMessageBox.critical(self, "Connection Timeout", "Backend server took too long to respond.")
            print("Frontend Debug (Coordinator - Login): Timeout: Backend server did not respond in time.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                if e.response:
                    error_json = e.response.json()
                    error_message += f" - {error_json.get('message', e.response.text)}"
                else:
                    error_message += f" - No readable response received."
            except requests.exceptions.JSONDecodeError:
                if e.response:
                    error_message += f" - Raw response: {e.response.text}"
                else:
                    error_message += f" - No readable response received."
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
            print(f"Frontend Debug (Coordinator - Login): HTTP error: {error_message}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred during login: {e}")
            print(f"Frontend Debug (Coordinator - Login): Unexpected error: {e}")

    def _handle_registration_attempt(self, registration_data):
        """
        Handles the registration attempt by making a request to the backend.
        """
        backend_url = "http://127.0.0.1:5000/register"

        print(f"Frontend Debug (Coordinator - Register): Sending data to backend: {registration_data}")

        response = None
        try:
            response = requests.post(backend_url, json=registration_data, timeout=5)
            response.raise_for_status()

            response_data = response.json()
            print(f"Frontend Debug (Coordinator - Register): Received response: {response_data}")

            if response.status_code == 201:
                QtWidgets.QMessageBox.information(self, "Registration Success", response_data.get("message", "Registration successful!"))
                self.register_page.clear_fields()
                self.show_login_page()
            else:
                QtWidgets.QMessageBox.warning(self, "Registration Failed", response_data.get("message", "Registration failed."))

        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error",
                                           "Could not connect to the backend server. Please ensure Flask app is running.")
            print("Frontend Debug (Coordinator - Register): ConnectionError: Backend server unreachable.")
        except requests.exceptions.Timeout:
            QtWidgets.QMessageBox.critical(self, "Connection Timeout", "Backend server took too long to respond.")
            print("Frontend Debug (Coordinator - Register): Timeout: Backend server did not respond in time.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                if e.response:
                    error_json = e.response.json()
                    error_message += f" - {error_json.get('message', e.response.text)}"
                else:
                    error_message += f" - No readable response received."
            except requests.exceptions.JSONDecodeError:
                if e.response:
                    error_message += f" - Raw response: {e.response.text}"
                else:
                    error_message += f" - No readable response received."
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
            print(f"Frontend Debug (Coordinator - Register): HTTP error: {error_message}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred during registration: {e}")
            print(f"Frontend Debug (Coordinator - Register): Unexpected error: {e}")


    def show_login_page(self):
        self.stacked_widget.setCurrentWidget(self.login_page) # Use self.stacked_widget
        self.setWindowTitle("MindZap - Login")
        self.current_username = None
        self.current_user_id = None
        # Close/reset dashboard if it exists and we're returning to login
        if self.dashboard_window:
            self.dashboard_window.close() # Close the dashboard QMainWindow
            self.dashboard_window = None # Clear the reference
        print("Switched to Login Page")

    def show_register_page(self):
        self.stacked_widget.setCurrentWidget(self.register_page) # Use self.stacked_widget
        self.setWindowTitle("MindZap - Register")
        print("Switched to Register Page")

    def show_dashboard_page(self, username: str, user_id: int):
        """
        Initializes and displays the dashboard, passing user info.
        This method is called after a successful login.
        """
        # Create dashboard window only if it doesn't exist (first login)
        if not self.dashboard_window:
            # MainApplicationWindow itself IS the dashboard_window in this setup
            self.dashboard_window = MainApplicationWindow(username, user_id, self) # Pass self (Coordinator)
            # Add the new dashboard QMainWindow to the coordinator's stacked widget
            self.stacked_widget.addWidget(self.dashboard_window)
            print(f"Dashboard window created and added for user: {username}, ID: {user_id}")
        else:
            # If dashboard already exists (e.g., returning after logout), update its user info
            self.dashboard_window.current_username = username
            self.dashboard_window.current_user_id = user_id
            self.dashboard_window.dashboard_ui.set_username_display(username)
            # Re-initialize specific pages if they need user_id update after login
            # These checks are important to ensure the methods exist before calling them
            # and that the pages are indeed the expected custom widget types.
            if hasattr(self.dashboard_window.dashboard_ui.page_2, 'set_current_user_id') and isinstance(self.dashboard_window.dashboard_ui.page_2, FlashcardPage):
                self.dashboard_window.dashboard_ui.page_2.set_current_user_id(user_id)
            if hasattr(self.dashboard_window.dashboard_ui.page_3, 'set_current_user_id') and isinstance(self.dashboard_window.dashboard_ui.page_3, QuizUiForm):
                self.dashboard_window.dashboard_ui.page_3.set_current_user_id(user_id)

        # Switch the coordinator's stacked widget to display the dashboard
        self.stacked_widget.setCurrentWidget(self.dashboard_window)
        self.setWindowTitle(f"MindZap - Dashboard ({username})")
        print(f"Switched to Dashboard Page for user: {username}")


if __name__ == '__main__':
    # Initialize and run the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)
    coordinator = ApplicationCoordinator()
    coordinator.show() # Show the main coordinator window
    sys.exit(app.exec_())