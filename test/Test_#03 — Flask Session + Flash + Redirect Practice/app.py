from flask import Flask, render_template, flash, get_flashed_messages,redirect,request,session,url_for
app=Flask(__name__)
app.secret_key="nabeel"
@app.route("/",methods=["POST","GET"])
@app.route("/login",methods=["POST","GET"])
def login():
   
   if request.method=="POST":
      user=request.form.get("name")
      pswd=request.form.get("password")
      if not user or not pswd:
         flash("Plase fill all fields")
         return redirect(url_for("login"))
      if user=="nabeel" and pswd=="secret":
         session['user']=user
         flash("login successfully")
         return redirect(url_for("home"))
      else :
         flash("user not found")
         return redirect(url_for("login"))
   return render_template("login.html")
@app.route("/home")
def home():
   print("test")
   if 'user' not in session:
      flash("user not founde","info")
      return redirect(url_for("login"))
   return render_template("home.html",user=session['user'])
@app.route("/logout")
def  logout():
   session.pop('user',None)
   flash("logut successfully ")
   return redirect(url_for("login"))
if  __name__=="__main__" :
   app.run(debug=True)