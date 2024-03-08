from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

db = "istreamradio.sqlite"

con = sqlite3.connect(db)
c = con.cursor()
con.close()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
