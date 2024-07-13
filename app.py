import sqlite3

from flask import Flask, render_template, url_for, json, jsonify

app = Flask(__name__)

db = "istreamradio.sqlite"
con = sqlite3.connect(db)
c = con.cursor()


radioList = list()
nowPlaying = list()


def populateList():
    radioList.clear()

    con = sqlite3.connect(db)
    c = con.cursor()

    for radioData in c.execute("select * from radiok"):
        radioList.append(
            {
                "id": radioData[0],
                "name": radioData[1],
                "url": radioData[2],
                "logo_thumbnail": radioData[3],
                "logo_large": radioData[4],
            }
        )
    con.close()


def setPlayer(id):
    nowPlaying.clear()
    con = sqlite3.connect(db)
    c = con.cursor()

    c.execute("select * from radiok where id = ?", [id])
    radioData = c.fetchone()
    nowPlaying.append(
        {
            "id": radioData[0],
            "name": radioData[1],
            "url": radioData[2],
            "logo_thumbnail": radioData[3],
            "logo_large": radioData[4],
        }
    )

    con.close()


@app.route("/")
def index():
    populateList()
    return render_template("index.html", radioList=radioList, nowPlaying=None)


@app.route("/listen/<int:id>")
def listen(id):
    populateList()
    setPlayer(id)
    # return jsonify(nowPlaying)
    return render_template("index.html", radioList=radioList, nowPlaying=nowPlaying)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
