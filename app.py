import os
import random

from dotenv import load_dotenv
from flask import Flask, render_template
from markupsafe import Markup

from desculpas_csv import load_existing_excuses

app = Flask(__name__)


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
