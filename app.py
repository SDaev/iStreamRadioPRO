import sqlite3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

db = "istreamradio.sqlite"
con = sqlite3.connect(db)
c = con.cursor()


@app.route("/")
def index():
    con = sqlite3.connect(db)
    c = con.cursor()

    radiok = []
    for r in c.execute("select * from radiok"):
        radiok.append(
            {
                "id": r[0],
                "name": r[1],
                "url": r[2],
                "logo_thumbnail": r[3],
                "logo_large": r[4],
            }
        )

    c.execute("select * from radiok where id = 0")
    r = c.fetchone()

    con.close()
    return render_template(
        "index.html",
        radiok=radiok,
        radio={
            "id": r[0],
            "name": r[1],
            "url": r[2],
            "logo_thumbnail": r[3],
            "logo_large": r[4],
        },
    )


@app.route("/lejatszas/<int:id>")
def lejatszas(id):
    con = sqlite3.connect(db)
    c = con.cursor()

    radiok = []
    for r in c.execute("select * from radiok"):
        radiok.append(
            {
                "id": r[0],
                "name": r[1],
                "url": r[2],
                "logo_thumbnail": r[3],
                "logo_large": r[4],
            }
        )

    c.execute("select * from radiok where id = ?", [id])
    r = c.fetchone()

    con.close()
    return render_template(
        "index.html",
        radiok=radiok,
        radio={
            "id": r[0],
            "name": r[1],
            "url": r[2],
            "logo_thumbnail": r[3],
            "logo_large": r[4],
        },
    )


if __name__ == "__main__":
    app.run(debug=True)
