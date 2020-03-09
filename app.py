from flask import Flask, render_template
import pandas as pd

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.route(debug = true)
