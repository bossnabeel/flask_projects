from flask import Flask, flash,render_template,request,redirect,url_for,get_flashed_messages
app=Flask(__name__)
app.secret_key="test"
@app.route("/",methods=["POST","GET"])
def auth():
    if request.method=="POST":
        user=request.form.get("name")
        pswd=request.form.get("password")
        if not user or not pswd:
            flash("fill all the fields")
            return redirect(url_for("auth"))
        if user=="admin" and pswd=="secret":
            return "home"
        else :
            flash("User not founded \n try again")
            return redirect(url_for("auth"))

    return render_template("index.html")
app.run()