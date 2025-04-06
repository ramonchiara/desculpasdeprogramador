import os
import random
import signal
import sys
import time

import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from desculpas_csv import load_existing_excuses, save_excuse


def get_a_programming_excuse():
    excuse = None
    url = "http://programmingexcuses.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        excuse_link = soup.find("a")
        if excuse_link:
            excuse = excuse_link.text.strip()
    return excuse


def translate_to_portuguese(openai_client, excuse):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """Você é um tradutor especializado em traduzir desculpas de programadores do inglês para o português.
Preserve o tom humorístico e a intenção original da mensagem."""
            },
            {
                "role": "user",
                "content": excuse
            }
        ]
    )
    return response.choices[0].message.content.strip()


def sleep_randomly():
    time.sleep(random.uniform(0.1, 2))


def main():
    load_dotenv()

    # Manipula o sinal de interrupção para garantir que o arquivo CSV fique íntegro ao sair.
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))

    excuses_csv = os.getenv("EXCUSES_CSV")
    excuses = load_existing_excuses(excuses_csv)
    excuses = {row[0] for row in excuses}
    print(f"Arquivo {excuses_csv} carregado com {len(excuses)} desculpas...")
    print()

    api_key = os.getenv("OPENAI_API_KEY")
    openai_client = openai.OpenAI(api_key=api_key)

    while True:
        excuse = get_a_programming_excuse()
        if excuse and excuse not in excuses:
            translated_excuse = translate_to_portuguese(openai_client, excuse)
            save_excuse(excuses_csv, excuse, translated_excuse)
            excuses.add(excuse)
            print(f"Nova desculpa: {excuse}")
            print(f"Traduzida....: {translated_excuse}")
        else:
            print(f"Desculpa velha... ({excuse})")

        # Tentativa de não parecer um robô
        sleep_randomly()


if __name__ == "__main__":
    main()
