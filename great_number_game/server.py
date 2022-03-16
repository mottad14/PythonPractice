from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "youShallNotPass...maybe"


######Renders Form
@app.route('/')
def index():
    if ("comp_guess") in session:
        print("The randomized number is", session["comp_guess"])
    else:
        session["comp_guess"] = random.randint(1,100)

    if "comparison" not in session:
        session["comparison"] = "none"
    else:
        print ("the current comparison is", session["comparison"])

    return render_template("index.html")

#### PROCESS FORM
@app.route("/process_guess", methods = ["POST"])
def process():
    print(request.form)
    user_guess = int(request.form["guess"])
    comp_guess = session["comp_guess"]

    if comp_guess > user_guess:
        session["comparison"] = "low"
    elif comp_guess < user_guess:
        session["comparison"] = "high"
    else:
        session["comparison"] = "perfect"
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)