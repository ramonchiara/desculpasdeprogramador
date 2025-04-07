import os

from dotenv import load_dotenv
from flask import Flask, render_template
from markupsafe import Markup

from desculpas_csv import get_random_excuse

app = Flask(__name__)


@app.route("/")
def index():
    excuses_csv = os.getenv("EXCUSES_CSV")
    excuse, translated_excuse = get_random_excuse(excuses_csv)
    translated_excuse = Markup(translated_excuse.replace("\n", "<br/>"))
    return render_template("index.html", translated_excuse=translated_excuse)


def main():
    if not load_dotenv():
        print("Você precisa configurar o arquivo .env antes...")
        exit(1)
    app.run(debug=True)


if __name__ == "__main__":
    main()
