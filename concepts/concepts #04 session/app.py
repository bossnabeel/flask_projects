from flask import Flask, render_template,redirect,flash,get_flashed_messages,request,url_for,session
app=Flask(__name__)
app.secret_key="nabeel"

@app.route("/", methods=["POST","GET"])
def login():
   if request.method=="POST":
      user=request.form.get("name")
      pswd=request.form.get("password")
      if not user or not pswd:
         flash("Fill all the fields !")
         return redirect(url_for("login"))
      if user and pswd:
         session['user']=user
         flash("Login successfully")
         return redirect(url_for("home"))
      else :
          flash("try again later")
          return redirect(url_for("login"))       
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/logout")
def logout():
   session.pop('user',None)
   flash("logout success")
   return redirect(url_for("login"))
   
if  __name__=="__main__" :
   app.run(debug=True)