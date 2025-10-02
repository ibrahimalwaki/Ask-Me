DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    filename TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(title, filename)  -- Ensures same book isn't added multiple times
);

CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    asked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

-- Add index for faster question lookups
CREATE INDEX idx_questions_book ON questions(book_id);
CREATE INDEX idx_questions_time ON questions(asked_at);
