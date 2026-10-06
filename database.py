import sqlite3
from datetime import datetime


class InterviewDatabase:

    def __init__(self, database_name="interview.db"):

        self.database_name = database_name

        self.create_table()

    def get_connection(self):

        return sqlite3.connect(
            self.database_name
        )

    def create_table(self):

        connection = self.get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS interviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                evaluation TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)

        connection.commit()

        connection.close()

    def save_interview(
        self,
        question,
        answer,
        evaluation
    ):

        connection = self.get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO interviews
            (question, answer, evaluation, date)
            VALUES (?, ?, ?, ?)
        """, (
            question,
            answer,
            evaluation,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        connection.commit()

        connection.close()

    def get_all_interviews(self):

        connection = self.get_connection()

        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM interviews
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]