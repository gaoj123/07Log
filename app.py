from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def root():
    return render_template("form.html")

@app.route("/response", methods=["POST","GET"])
def response():
    print request.method
    print request.headers
    print request.form
    username=request.form["Name"]
    password=request.form["Password"]
    status=validate(username,password)
    if status==0:
        return render_template("response.html", name=username)
    elif status==1:
        return render_template("form.html",message="Wrong Password")
    else:
        return render_template("form.html",message="Wrong Username")
    

def validate(username, password):
    if username == "DW":
        if password == "kittens":
            return 0 #everything correct
        return 1 #wrong password
    return 2 # wrong username

if __name__=="__main__":
    app.debug=True
    app.run()
