import os

from dotenv import load_dotenv

from desculpas_csv import load_existing_excuses
from desculpas_db import create_table, insert_excuses, DbError


def load_excuses_into_db():
    excuses_csv = os.getenv("EXCUSES_CSV")
    excuses = load_existing_excuses(excuses_csv)
    print(f"Arquivo {excuses_csv} carregado com {len(excuses)} desculpa(s)...")

    n = insert_excuses(excuses)
    print(f"{n} nova(s) desculpa(s) inserida(s) no banco!")


def main():
    if not load_dotenv():
        print("Você precisa configurar o arquivo .env antes...")
        exit(1)

    try:
        if create_table():
            print("Tabela \"desculpas\" criada com sucesso!")
        else:
            print("Tabela \"desculpas\" já existia!")
        load_excuses_into_db()
        print("Banco de dados inicializado com sucesso!")
    except DbError as ex:
        print(ex)


if __name__ == "__main__":
    main()
