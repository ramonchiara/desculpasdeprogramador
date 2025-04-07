from dotenv import load_dotenv
from flask import Flask, render_template
from markupsafe import Markup

from desculpas_db import get_random_excuse, DbError

app = Flask(__name__)


@app.route("/")
def index():
    try:
        excuse, translated_excuse = get_random_excuse()
        translated_excuse = Markup(translated_excuse.replace("\n", "<br/>"))
    except DbError as ex:
        excuse = "T_T"
        translated_excuse = str(ex)
    return render_template("index.html", excuse=excuse, translated_excuse=translated_excuse)


def main():
    if not load_dotenv():
        print("Você precisa configurar o arquivo .env antes...")
        exit(1)
    app.run(debug=True)


if __name__ == "__main__":
    main()
