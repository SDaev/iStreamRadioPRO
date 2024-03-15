from flask import Flask, render_template
import base64
import sqlite3

app = Flask(__name__)

db = "istreamradio.sqlite"

con = sqlite3.connect(db)
c = con.cursor()
con.close()

nowplaying = 0


@app.route("/")
def index():
    con = sqlite3.connect(db)
    c = con.cursor()

    nowplaying == 0
    radiok = []
    for r in c.execute("select * from radiok"):
        radiok.append({"id": r[0], "name": r[1], "url": r[2], "logo": r[3]})
    con.close()
    return render_template("index.html", radiok=radiok)


@app.route("/<int:id>", methods=["POST"])
def play(id):
    pass
    nowplaying == id


if __name__ == "__main__":
    app.run(debug=True)
