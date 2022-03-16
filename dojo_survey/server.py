from operator import methodcaller
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "youShallNotPass...maybe"

######Renders Form
@app.route('/')
def index():
    return render_template("index.html")


###Results Form
@app.route('/result', methods = ["POST"])
def results():
    print ("This is the request form",request.form)
    print ("This is the session form", session)
    session['name'] = request.form['name'] 
    session['location'] = request.form['location']
    session['language'] = request.form['language'] 
    session['comments'] = request.form['comments'] 

    return render_template("result.html")

##Reset form - clears session data and routes back to starting page   
@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)

