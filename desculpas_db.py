import os

import psycopg2
from psycopg2 import OperationalError
from psycopg2.errors import DuplicateTable
from psycopg2.extras import execute_batch


class DbError(Exception):
    def __str__(self):
        return "Isto não é uma desculpa: não estou conseguindo acessar o banco!"


def get_db_config():
    return {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT", "5432"),
    }


def create_table():
    created = False
    try:
        db_config = get_db_config()
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    create table desculpas (
                        original text primary key,
                        traduzida text not null
                    )
                    """
                )
            conn.commit()
            created = True
    except OperationalError:
        raise DbError()
    except DuplicateTable:
        pass
    return created


def insert_excuses(excuses):
    try:
        db_config = get_db_config()
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                execute_batch(
                    cursor,
                    "insert into desculpas (original, traduzida) values (%s, %s) on conflict (original) do nothing returning original",
                    excuses
                )
                inserted = cursor.fetchall()
            conn.commit()
        return len(inserted)
    except OperationalError:
        raise DbError()


def get_random_excuse():
    try:
        # excuse = (None, None)
        db_config = get_db_config()
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("select original, traduzida from desculpas order by random() limit 1")
                excuse = cursor.fetchone()
        return excuse
    except OperationalError:
        raise DbError()
