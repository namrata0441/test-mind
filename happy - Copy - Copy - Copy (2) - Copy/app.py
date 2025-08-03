import os
import sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timezone  # Import timezone for UTC datetimes
import json  # Import json for parsing/serializing if complex data needs to be stored

# --- Initialize Flask App ---
app = Flask(__name__)

# --- Database Configuration ---
# Get the directory of the current script (backend folder)
basedir = os.path.abspath(os.path.dirname(__file__))
# Construct the path to the database file in the backend folder
# This will use 'mindzap.db' inside the backend folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mindzap.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for performance

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# --- Database Models ---
class User(db.Model):
    __tablename__ = 'users'  # Explicitly set table name to 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # 'username' is the email for login
    password = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20))
    country = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Use timezone.utc

    # One-to-many relationship with Flashcard
    flashcards = db.relationship('Flashcard', backref='user', lazy=True)
    # One-to-many relationship with Quiz
    quizzes = db.relationship('Quiz', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'  # Use username (email) for representation


class Flashcard(db.Model):
    __tablename__ = 'flashcards' # Explicitly define tablename
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False,
                         default=lambda: datetime.now(timezone.utc))  # Use timezone.utc
    interval = db.Column(db.Integer, default=1)
    repetitions = db.Column(db.Integer, default=0)
    ease_factor = db.Column(db.Float, default=2.5)

    def __repr__(self):
        return f'<Flashcard {self.question}>'


class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    questions_data = db.Column(db.Text, nullable=False)  # Stores JSON string of questions

    def __repr__(self):
        return f'<Quiz {self.title}>'


# --- API Endpoints ---

@app.route('/')
def home():
    return jsonify(message="Welcome to the MindZap Backend API!")


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(f"Backend Debug (Register): Received data: {data}")

    username = data.get('username')  # Frontend sends email as 'username'
    password = data.get('password')
    full_name = data.get('full_name')
    phone_number = data.get('phone_number')
    country = data.get('country')

    if not all([username, password, full_name, phone_number, country]):
        print("Backend Debug (Register): Missing fields.")
        return jsonify(message="All fields are required for registration."), 400

    if User.query.filter_by(username=username).first():  # Check uniqueness for username (email)
        print(f"Backend Debug (Register): Username (email) {username} already taken.")
        return jsonify(message="Username (email) already taken."), 409

    new_user = User(
        username=username,  # Assign to username (email) field
        password=password,  # Assign to password field
        full_name=full_name,
        phone_number=phone_number,
        country=country
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        print(f"Backend Debug (Register): User {username} registered successfully!")
        return jsonify(message="User registered successfully!"), 201
    except Exception as e:
        db.session.rollback()
        print(f"Backend Debug (Register): Registration failed: {str(e)}")
        return jsonify(message=f"Registration failed: {str(e)}"), 500


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(f"Backend Debug (Login): Received data: {data}")

    username = data.get('username')  # Frontend sends username (email) here
    password = data.get('password')

    if not username or not password:
        print("Backend Debug (Login): Missing username or password.")
        return jsonify(message="Username and password are required."), 400

    user = User.query.filter_by(username=username).first()

    if user:
        print(f"Backend Debug (Login): User found: {user.username}.")
        # In a real app, you would hash and verify passwords securely (e.g., using bcrypt)
        if user.password == password:
            print(f"Backend Debug (Login): Login successful for {username}.")
            # Return user_id along with username for frontend to use with quiz/flashcard creation
            return jsonify(message=f"Login successful! Welcome, {username}", username=user.username,
                           user_id=user.id), 200
        else:
            print(f"Backend Debug (Login): Invalid password for {username}.")
            return jsonify(message="Invalid username or password."), 401
    else:
        print(f"Backend Debug (Login): User {username} not found in database.")
        return jsonify(message="Invalid username or password."), 401


@app.route('/profile/<username>', methods=['GET'])
def get_user_profile(username):
    """
    Retrieves a user's profile data from the database.
    """
    print(f"Backend Debug (Profile GET): Request for username (email): {username}")
    user = User.query.filter_by(username=username).first()
    if user:
        print(f"Backend Debug (Profile GET): User found: {user.full_name}")
        return jsonify({
            'username': user.username,  # Return username (email) for frontend consistency
            'full_name': user.full_name,
            'phone_number': user.phone_number,
            'country': user.country,
            'created_at': user.created_at.isoformat()
        }), 200
    else:
        print(f"Backend Debug (Profile GET): User not found."), 404


@app.route('/profile/update', methods=['POST'])
def update_profile():
    data = request.get_json()
    print(f"Backend Debug (Profile UPDATE): Received data: {data}")

    if not data:
        print("Backend Debug (Profile UPDATE): No data received.")
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    user_username = data.get('username')  # Frontend sends username (email) to identify the user
    if not user_username:
        print("Backend Debug (Profile UPDATE): Username (email) missing in update data.")
        return jsonify({"status": "error", "message": "Username (email) is required to update profile."}), 400

    user = User.query.filter_by(username=user_username).first()

    if not user:
        print(f"Backend Debug (Profile UPDATE): User {user_username} not found for update.")
        return jsonify({"status": "error", "message": "User not found for update"}), 404

    try:
        # Update fields only if they are provided in the incoming data
        user.full_name = data.get('full_name', user.full_name)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.country = data.get('country', user.country)
        # Email (username) is generally not updated via profile update, but via separate process.

        db.session.commit()
        print(f"Backend Debug (Profile UPDATE): Profile for {user_username} updated successfully.")
        return jsonify({"status": "success", "message": "Profile updated successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Backend Debug (Profile UPDATE): Error updating profile for {user_username}: {e}")
        return jsonify({"status": "error", "message": f"Failed to update profile: {str(e)}"}), 500


@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    # This endpoint should ideally filter by user_id for the logged-in user
    # For now, it returns all flashcards.
    flashcards = Flashcard.query.all()
    output = []
    for flashcard in flashcards:
        output.append({
            'id': flashcard.id,
            'user_id': flashcard.user_id,
            'question': flashcard.question,
            'answer': flashcard.answer,
            'due_date': flashcard.due_date.isoformat(),
            'interval': flashcard.interval,
            'repetitions': flashcard.repetitions,
            'ease_factor': flashcard.ease_factor
        })
    return jsonify(output), 200


@app.route('/flashcards', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    user_id = data.get('user_id')  # In a real app, this would come from an authenticated session
    question = data.get('question')
    answer = data.get('answer')

    if not user_id or not question or not answer:
        return jsonify(message="User ID, question, and answer are required."), 400

    new_flashcard = Flashcard(user_id=user_id, question=question, answer=answer)
    try:
        db.session.add(new_flashcard)
        db.session.commit()
        return jsonify(message="Flashcard added successfully!", id=new_flashcard.id), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(message=f"Failed to add flashcard: {str(e)}"), 500


@app.route('/quizzes', methods=['POST'])
def create_quiz():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description')
    questions_data = data.get('questions_data')

    if not all([user_id, title, questions_data]):
        return jsonify(message="User ID, title, and questions data are required to create a quiz."), 400

    try:
        # Ensure questions_data is a valid JSON string
        json.dumps(questions_data)
    except TypeError:
        return jsonify(message="Questions data must be a valid JSON array/object."), 400

    new_quiz = Quiz(
        user_id=user_id,
        title=title,
        description=description,
        questions_data=json.dumps(questions_data) # Store as JSON string
    )
    try:
        db.session.add(new_quiz)
        db.session.commit()
        return jsonify(message="Quiz created successfully!", id=new_quiz.id), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(message=f"Failed to create quiz: {str(e)}"), 500


@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    quizzes = Quiz.query.all()
    output = []
    for quiz in quizzes:
        output.append({
            'id': quiz.id,
            'user_id': quiz.user_id,
            'title': quiz.title,
            'description': quiz.description,
            'questions_data': json.loads(quiz.questions_data) # Load from JSON string
        })
    return jsonify(output), 200


@app.route('/quizzes/<int:quiz_id>', methods=['GET'])
def get_quiz_by_id(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    if quiz:
        return jsonify({
            'id': quiz.id,
            'user_id': quiz.user_id,
            'title': quiz.title,
            'description': quiz.description,
            'questions_data': json.loads(quiz.questions_data)
        }), 200
    else:
        return jsonify(message="Quiz not found."), 404


@app.route('/update_credentials', methods=['POST'])
def update_credentials():
    data = request.get_json()
    print(f"Backend Debug (Update Credentials): Received data: {data}")

    current_username = data.get('current_username')  # The current email of the logged-in user
    new_username = data.get('new_username')  # The new email (if changed)
    new_password = data.get('new_password')  # The new password (if changed)

    if not current_username:
        return jsonify(message="Current username (email) is required for update."), 400

    user = User.query.filter_by(username=current_username).first()
    if not user:
        print(f"Backend Debug (Update Credentials): User {current_username} not found.")
        return jsonify(message="User not found."), 404

    try:
        # Update email if a new one is provided and it's different
        if new_username and new_username != current_username:
            # Check if the new username (email) is already taken by another user
            if User.query.filter_by(username=new_username).first():
                return jsonify(message="New email already taken by another user."), 409
            user.username = new_username
            print(f"Backend Debug (Update Credentials): Email updated from {current_username} to {new_username}")

        # Update password if a new one is provided
        if new_password:
            user.password = new_password  # In a real app, hash this password!
            print(f"Backend Debug (Update Credentials): Password updated for {user.username}")

        db.session.commit()
        print(f"Backend Debug (Update Credentials): Credentials updated successfully for {user.username}")
        return jsonify(message="Credentials updated successfully!"), 200
    except Exception as e:
        db.session.rollback()
        print(f"Backend Debug (Update Credentials): Error updating profile for {user.username}: {e}")
        return jsonify({"status": "error", "message": f"Failed to update profile: {str(e)}"}), 500


# --- Main Run Block with Error Handling ---
if __name__ == '__main__':
    try:
        db_path = os.path.join(basedir, 'mindzap.db')
        with app.app_context():
            # Create database tables if they don't exist
            if not os.path.exists(db_path):
                print(
                    f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Database file '{db_path}' not found. Creating a new one and tables...")
                try:
                    db.create_all()
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Tables created successfully in new database.")
                except Exception as e:
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Error creating tables in new database: {e}",
                        file=sys.stderr)
                    sys.exit(1)
            else:
                print(
                    f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Database file '{db_path}' already exists. Attempting to ensure tables are present...")
                try:
                    db.create_all() # This will create tables if they are missing in an existing DB
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Tables checked/created successfully in existing database (or created if missing).")
                except Exception as e:
                    # This might catch "table already exists" errors, which are fine if tables are already there.
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Error ensuring tables in existing database. This might be because tables already exist, which is okay: {e}",
                        file=sys.stderr)
                    pass  # Allow the app to continue if tables already exist.

        print(
            f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Attempting to run Flask app...")
        app.run(debug=True, port=5000)
    except Exception as e:
        print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] !!! ERROR STARTING FLASK APP !!!",
              file=sys.stderr)
        print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Error details: {e}",
              file=sys.stderr)
        import traceback

        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
