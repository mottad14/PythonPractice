from flask import Flask, render_template      # Imports Flask and html template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/dojo')
def success():
  return "Dojo!"
    
@app.route('/say/<string:name>') # this route capitalizes whatever string is passed in for name
def hello(name):
    print(name)
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:phrase>') # this route displays the phrase passed in the number of times num is
def repeat(num, phrase):
    print(num, phrase)
    return render_template('repeat.html', num = num, phrase = phrase)  


# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)    # Run the app in debug mode.

