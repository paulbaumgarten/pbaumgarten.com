from flask import Flask, send_file # import send_file here to use the command

app = Flask(__name__) # Set name

@app.route('/') # Signifies page
def index(): # '/' needs function 'index', otherwise name function same as route
    return "Hi there"

@app.route("/page2") # Type this next to 'localhost' to go to the page
def page2():
    return "This is page 2. This is fun"

@app.route("/page1")
def page1():
    return send_file('page1.html')

app.run(host='0.0.0.0', port=80, debug=True)