from dotenv import load_dotenv

import os
import signal
import sys

import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row


class DB:
    def __init__(self):
        load_dotenv()
        db_url = os.environ.get("DATABASE_URL")
        self.connection = psycopg.connect(
            db_url,
            row_factory=namedtuple_row
        )
        signal.signal(signal.SIGINT, self.graceful_shutdown)

    def graceful_shutdown(self):
        self.connection.close()

    def create_entry(self, photo:bytearray=None, cleaniness:float=None, active:bool=None, hours:str=None, review:str=None, address:str=None) -> bool:
        try:
            with self.connectionon.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS washrooms (id SERIAL PRIMARY KEY, photo bytea NULL, cleaniness real NOT NULL, active boolean NULL, hours text NOT NULL, review text NULL, address text NOT NULL)"
                )
                cursor.execute(
                    "INSERT INTO washrooms (photo, cleaniness, active, hours, review, address) VALUES (%s %s %s %s %s %s)", (photo, cleaniness, active, hours, review, address)
                )
        except Exception:
            return False
        return True
    
    def get_entries(self):
        washrooms = []
        try:
            with self.connection.cursor() as cursor:
                for row in cursor.execute("SELECT * FROM washrooms"):
                    washrooms.append(row)
        except Exception:
            return []
        return washrooms
    
    def update_entry(self, id:int, photo:bytearray=None, cleaniness:float=None, active:bool=None, hours:str=None, review:str=None, address:str=None) -> bool:
        if id is None or id < 0:
            return False
        