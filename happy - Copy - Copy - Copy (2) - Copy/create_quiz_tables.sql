-- create_quiz_tables.sql

-- Drop tables if they exist to allow for clean recreation
DROP TABLE IF EXISTS Answers;
DROP TABLE IF EXISTS Questions;
DROP TABLE IF EXISTS Categories;

-- Create Categories table
CREATE TABLE Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL UNIQUE
);

-- Create Questions table
CREATE TABLE Questions (
    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryID INTEGER NOT NULL,
    QuestionText TEXT NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Create Answers table
CREATE TABLE Answers (
    AnswerID INTEGER PRIMARY KEY AUTOINCREMENT,
    QuestionID INTEGER NOT NULL,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL, -- 0 for false, 1 for true
    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID)
);