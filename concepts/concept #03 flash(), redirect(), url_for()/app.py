from flask import Flask, redirect,flash,render_template,request,url_for
app=Flask(__name__)
app.secret_key="nabeel"

@app.route ("/",methods=["POST","GET"])
def auth():
    if request.method=="POST":
        user=request.form.get("name")
        passwd=request.form.get("password")
        if not user or not passwd:
            flash("Fill all fields")
            return redirect(url_for("auth"))
        if user=="admin" and passwd=="secret":
            flash ("login sucessfull")
            return "home"
        else :
            flash("invalid user OR password")
            return redirect(url_for("auth"))
            
    return render_template("index.html")

app.run(debug=True)
