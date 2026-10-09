
import sqlite3
from pathlib import Path

# Store the database inside the backend folder
DB_PATH = Path(__file__).resolve().parent.parent / "internships.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS internships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                title TEXT NOT NULL,
                location TEXT,
                url TEXT NOT NULL UNIQUE,
                description TEXT,
                match_score INTEGER,
                date_found TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                internship_id INTEGER NOT NULL UNIQUE,
                status TEXT NOT NULL DEFAULT 'saved',
                date_applied TIMESTAMP,
                resume_path TEXT,
                FOREIGN KEY (internship_id)
                    REFERENCES internships(id)
            )
        """)

        connection.commit()
        print("Database initialized successfully!")

    finally:
        connection.close()
