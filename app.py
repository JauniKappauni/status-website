from flask import Flask, render_template, request
from ping3 import verbose_ping

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    host = request.form.get("host")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)