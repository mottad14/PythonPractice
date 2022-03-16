from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'You shall not pass... maybe'

#RENDER THE FORM AT WHATEVER THE COUNT IS OR START AT 1 if session["count"] not found!
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    
    return render_template("index.html")

#ACTION -> BUTTON session DATA ROUTE HERE - increases visits by +2 by rerouting 
# and adding 1 (the rerouting visit adds 1 to the counter) -- name of submit buttons 
# are "change" - and values are "add" & 'reset' 
#Redirects back to main page
@app.route("/count", methods=["POST"])
def keepCount():
    print("I HAVE VISITED /COUNT")
    if request.form["change"]=="add":
        session["count"] += 1
    elif request.form["change"]=="reset":
        session["count"] = 0

    return redirect("/")

#RESETS SESSION COUNTER AND REDIRECTS BACK TO MAIN
@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True, port = 5001)

