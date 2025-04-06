import os
import random
import csv
from dotenv import load_dotenv
from flask import Flask, render_template
from markupsafe import Markup

app = Flask(__name__)


def load_existing_excuses(excuses_csv):
    excuses = set()
    try:
        with open(excuses_csv, newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader, None)  # skip header
            for row in reader:
                excuses.add((row[0], row[1]))
    except FileNotFoundError:
        pass
    return excuses


def get_random_excuse():
    excuses_csv = os.getenv("EXCUSES_CSV")
    excuses = load_existing_excuses(excuses_csv)
    excuse = random.choice(list(excuses))
    return excuse


@app.route("/")
def index():
    excuse, translated_excuse = get_random_excuse()
    translated_excuse = Markup(translated_excuse.replace("\n", "<br/>"))
    return render_template("index.html", translated_excuse=translated_excuse)


def main():
    load_dotenv()
    app.run(debug=True)


if __name__ == "__main__":
    main()
