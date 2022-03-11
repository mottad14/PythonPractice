from flask import Flask, render_template      # Imports Flask and html template
app = Flask(__name__)

@app.route('/play1/<int:num>/<string:color>')
def altogether(num, color):
    return render_template('play1.html', num = num, color = color)

@app.route("/play1/<int:num>")
def boxRepeat(num):
    return render_template('play1.html', num = num, color = "blue")

@app.route("/play1")
def hello_world():
    return render_template("play1.html", num = 3, color = "blue")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)