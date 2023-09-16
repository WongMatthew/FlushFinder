from dotenv import load_dotenv

import os
import signal
import inspect

import psycopg
from psycopg import sql
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

    def create_entry(self, cleaniness:float, address:str, hours:str, photo:bytearray=None, active:bool=None, review:str=None) -> bool:
        if cleaniness < 0 or cleaniness > 5:
            return False
        try:
            with self.connectionon.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS washrooms (id SERIAL PRIMARY KEY, cleaniness real NOT NULL, address text NOT NULL, hours text NOT NULL, photo bytea NULL, active boolean NULL, review text NULL)"
                )
                cursor.execute(
                    "INSERT INTO washrooms (cleaniness, addresss, hours, photo, active, review) VALUES (%s %s %s %s %s %s)", (cleaniness, address, hours, photo, active, review)
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
    
    def update_entry(self, id:int, cleaniness:float, address:str, hours:str, photo:bytearray=None, active:bool=None, review:str=None) -> bool:
        args = inspect.getfullargspec(self.update_entry).args
        args.remove("self")
        args.remove("id")
        filled_args = {k:v for k, v in locals().items() if k in args and v is not None}
        arg_keys = list(filled_args.keys())
        if id is None or id < 0:
            return False
        if cleaniness and (cleaniness < 0 or cleaniness > 5):
            return False
        try:
            with self.connectionon.cursor() as cursor:
                cursor.execute(
                    sql.SQL("UPDATE washrooms SET ({})=({}) WHERE {}={}").format(sql.SQL(", ").join(map(sql.Identifier, arg_keys)), sql.SQL(", ").join(map(sql.Placeholder, arg_keys)), sql.Identifier("id"), sql.Placeholder()),
                    filled_args, id
                )
        except Exception:
            return False
        return True
