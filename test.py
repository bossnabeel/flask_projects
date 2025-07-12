from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def method_name():
    return render_template("index.html")
