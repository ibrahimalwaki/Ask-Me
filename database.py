import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect("askmybook.db", check_same_thread=False)
cursor = conn.cursor()

def log_book(title, filename):
    """Save a book if it doesn't exist, return its ID"""
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO books (title, filename) VALUES (?, ?)",
            (title, filename)
        )
        conn.commit()
        
        # Get the ID whether it was just inserted or already existed
        cursor.execute(
            "SELECT id FROM books WHERE title = ? AND filename = ?",
            (title, filename)
        )
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Database error in log_book: {e}")
        conn.rollback()
        raise

def log_question(book_id, question, answer):
    """Save every Q&A interaction with timestamp"""
    try:
        cursor.execute(
            "INSERT INTO questions (book_id, question, answer) VALUES (?, ?, ?)",
            (book_id, question, answer)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Database error in log_question: {e}")
        conn.rollback()
        raise

def get_book_history(book_id, limit=20):
    """Retrieve Q&A history for a book"""
    try:
        cursor.execute(
            "SELECT question, answer, asked_at FROM questions "
            "WHERE book_id = ? ORDER BY asked_at DESC LIMIT ?",
            (book_id, limit)
        )
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error in get_book_history: {e}")
        raise

# Initialize database tables if they don't exist
def init_db():
    with open('schema.sql', 'r') as f:
        cursor.executescript(f.read())
    conn.commit()


# def delete_question(question_text, book_id):
#     """Delete a Q&A pair by question text and book ID"""
#     try:
#         cursor.execute(
#             "DELETE FROM questions WHERE book_id = ? AND question = ?",
#             (book_id, question_text)
#         )
#         conn.commit()
#     except sqlite3.Error as e:
#         print(f"Database error in delete_question: {e}")
#         conn.rollback()
#         raise
