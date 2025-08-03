import sys
from PyQt5 import QtWidgets
import requests  # Import requests for backend communication
import webbrowser

# Import your UI classes
from dashboard_form import Ui_MainWindow
# register_form and login_form are no longer imported here, as main.py handles them

# Import custom widgets that are instantiated within Ui_MainWindow's setupUi
from profile_widget import ProfileWidget
from aboutUs import AboutUsWidget
from setting import SettingsWidget
from flashcard_page import FlashcardPage
from quiz_form import QuizUiForm

class MainApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, username: str, user_id: int, coordinator: QtWidgets.QStackedWidget):
        super().__init__()
        self.setWindowTitle(f"MindZap Application - Dashboard ({username})")
        self.setGeometry(100, 100, 1024, 768)

        self.current_username = username
        self.current_user_id = user_id
        self.coordinator = coordinator # Reference to the coordinator for logout

        # Initialize Dashboard UI (Ui_MainWindow) and set it up on THIS QMainWindow
        self.dashboard_ui = Ui_MainWindow()
        self.dashboard_ui.setupUi(self)

        # Access the stackedWidget which is now an attribute of self.dashboard_ui
        self.dashboard_content_stacked_widget = self.dashboard_ui.stackedWidget

        # Set the username display label immediately
        self.dashboard_ui.set_username_display(self.current_username)

        self.init_connections()

        # Pass user_id to relevant dashboard pages if they need it
        if hasattr(self.dashboard_ui.page_2, 'set_current_user_id'): # FlashcardPage
            self.dashboard_ui.page_2.set_current_user_id(self.current_user_id)
        if hasattr(self.dashboard_ui.page_3, 'set_current_user_id'): # QuizUiForm
            self.dashboard_ui.page_3.set_current_user_id(self.current_user_id)
        # Add similar calls for any other pages that need user_id

    def init_connections(self):
        # Connect sidebar buttons from dashboard_ui to switch pages within its own stackedWidget
        self.dashboard_ui.home_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(0) if checked else None)
        self.dashboard_ui.home_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(0) if checked else None)

        self.dashboard_ui.flash_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(2) if checked else None)
        self.dashboard_ui.flash_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(2) if checked else None)

        self.dashboard_ui.quizze_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(3) if checked else None)
        self.dashboard_ui.quizze_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(3) if checked else None)

        self.dashboard_ui.about_btn_1.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(4) if checked else None)
        self.dashboard_ui.about_btn_2.toggled.connect(lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(4) if checked else None)

        # Settings buttons: connect to a method that also passes user email
        self.dashboard_ui.setting_1.toggled.connect(lambda checked: self.show_settings_page() if checked else None)
        self.dashboard_ui.setting_2.toggled.connect(lambda checked: self.show_settings_page() if checked else None)

        # Profile button: connect to a method that fetches and loads profile data
        self.dashboard_ui.user_btn.clicked.connect(self.show_profile_page)

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
            response = requests.get(backend_url)
            response.raise_for_status()
            profile_data = response.json()
            print(f"Frontend Debug (MainApp - Profile Fetch): Fetched profile: {profile_data}")
            return profile_data
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error", "Could not connect to backend to fetch profile.")
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
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred fetching profile: {e}")
        return None

    def perform_google_search(self):
        """Performs a Google search based on the input in the search bar."""
        if hasattr(self.dashboard_ui, 'search_input'):
            search_query = self.dashboard_ui.search_input.text().strip()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                print(f"Performed Google search for: {search_query}")
            else:
                QtWidgets.QMessageBox.information(self, "Search", "Please enter a search query.")
            self.dashboard_ui.search_input.clear()
        else:
            print("search_input not found in UI.")

    def show_settings_page(self):
        """
        This method is called when a settings button is clicked.
        It passes the current user's email to the SettingsWidget before displaying it.
        """
        if self.current_username:
            if hasattr(self.dashboard_ui.page_5, 'set_current_user_email') and isinstance(self.dashboard_ui.page_5, SettingsWidget):
                self.dashboard_ui.page_5.set_current_user_email(self.current_username)
                print(f"Debug MainApp: Passed email '{self.current_username}' to SettingsWidget.")
                self.dashboard_content_stacked_widget.setCurrentIndex(5)
                self.setWindowTitle(f"MindZap - Settings ({self.current_username})")
                print(f"Switched to Settings Page for user: {self.current_username}")
            else:
                QtWidgets.QMessageBox.warning(self, "Settings Error", "Settings widget not found or not initialized correctly.")
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
                if hasattr(self.dashboard_ui.page_7, 'load_profile_data') and isinstance(self.dashboard_ui.page_7, ProfileWidget):
                    self.dashboard_ui.page_7.load_profile_data(profile_data)
                    self.dashboard_content_stacked_widget.setCurrentIndex(1)
                    self.setWindowTitle(f"MindZap - Profile ({self.current_username})")
                    print(f"Switched to Profile Page for user: {self.current_username}")
                else:
                    QtWidgets.QMessageBox.warning(self, "Profile Error", "Profile widget not found or not initialized correctly.")
            else:
                QtWidgets.QMessageBox.warning(self, "Profile Error", "Could not load profile data.")
        else:
            QtWidgets.QMessageBox.warning(self, "Profile Error", "No user logged in to view profile.")
            self.coordinator.show_login_page() # Redirect to login if no user is logged in

# The __main__ block is now in main.py
