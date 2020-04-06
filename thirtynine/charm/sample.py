from flask import Flask,templating,request
import pickle

with open("vect.pickle","rb") as f:
    vect=pickle.load(f)

with open("nb.pickle","rb") as f:
    nb=pickle.load(f)

app=Flask("hell")

@app.route("/form/")
def fom():
    return templating.render_template("index.html")

@app.route("/submit/",methods=["POST"])
def submit():
    message=request.form["message"]
    x_data=vect.transform([message]).todense()
    y=nb.predict(x_data)
    print(y)
    return str(y)


