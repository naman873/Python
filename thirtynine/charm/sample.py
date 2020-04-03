from flask import Flask,templating,request

app=Flask("hell")
@app.route("/form/")

def fom():
    return templating.render_template("index.html")

@app.route("/submit/",methods=["POST"])
def submit():
    fname=request.args.get("firstname")
    lname = request.args.get("password")
    return "my first name is {} and last name is {}".format(fname,lname)

