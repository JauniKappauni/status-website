from flask import Flask, render_template, request
from ping3 import ping

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    status = ""
    output = ""
    if request.method == "POST":
        host = request.form.get("host")
        status = ping(host)
        output = "online" if status else "offline"
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)