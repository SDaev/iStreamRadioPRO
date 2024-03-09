from flask import Flask, render_template
import base64
import sqlite3

app = Flask(__name__)

db = "istreamradio.sqlite"

con = sqlite3.connect(db)
c = con.cursor()
con.close()


@app.route("/")
def index():
    con = sqlite3.connect(db)
    c = con.cursor()

    radiok = []
    for r in c.execute("select * from radiok"):
        logo_bytes = bytes.fromhex(r[3])
        logo_b64 = base64.b64encode(logo_bytes).decode()
        radiok.append(
            {"name": r[0], "frequency": r[1], "description": r[2], "logo": logo_b64}
        )
    con.close()
    return render_template("index.html", radiok=radiok)


if __name__ == "__main__":
    app.run(debug=True)
