from flask import Flask, render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25),unique=True)
    password=db.Column(db.String(25))
    @app.route("/login",methods=["POST","GET"])
    def login():
        if request.method=="POST":
            name=request.form["username"]
            pswd=request.form["password"]
            new_user=User(username=name,password=pswd)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/home")
        return render_template("login.html")
@app.route("test/")
def test():
     db.session.query.all()
     

@app.route("/home",methods=["POST","GET"]) 
def home():
    return render_template("home.html")

if  __name__=="__main__":
    app.run(debug=True)
