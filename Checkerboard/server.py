from flask import Flask, render_template      # Imports Flask and html template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", rows = 8, columns =8)

@app.route('/<int:rows>/<int:columns>')
def altogether(rows, columns):
    return render_template('index.html', rows = rows, columns = columns)

@app.route("/<int:rows>")
def boxRepeat(rows):
    return render_template('index.html', rows =rows, columns = 8)







if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)

