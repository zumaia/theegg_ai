from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

# otro
@app.route("/video")
def video():
    return render_template("video.html")

# material
@app.route("/material")
def material():
    return render_template("material.html")


@app.route("/historia")
def disclimer():
    return render_template("historia.html")


