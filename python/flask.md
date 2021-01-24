# Flask - Web server

So much of modern programming involves the web, no handbook would be complete without a look at how to use Python on the web. Python can be used to build a web server quite easily through the freely available Flask library.

The client side of the web (what the user runs in their web browser) remains a combination of HTML, CSS and Javascript. No amount of Python will avoid that. That is also where the added complication comes in, as suddenly you aren't just learning Python but you'll have to learn those other three languages as well. That added complexity is actually one of the big reasons why I switched to Python away from Javascript as my "introduction to programming" language with students.

I will focus on the Python. If you are a student of mine, I can help point you in the direction of suitable tutorials for the Javascript, HTML and CSS, but I won't get into it here. I'll simply give you the demo code for those three without much explanation.

By the end, we'll have made ourselves a nice little Chat Application.

Good references for Flask:

* https://www.tutorialspoint.com/flask/
* http://flask.pocoo.org/docs/1.0/

## A basic web server

At it's most basic, a Flask webserver might look like this in Python:

```python
from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'booyeah!secret!'

@app.route('/')
def home():
    return send_file("main.html")

@app.route('/about')
def about():
    return send_file("about.html")

@app.route('/products')
def products():
    return send_file("products.html")

@app.route('/user/<userid>')
def products(userid):
    return "You are looking at the page for "+userid

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

* The app variable contains the Flask system.
* The `@app.route("/location")` is how you specify all the file/folder locations that will be accessible. Each of these must be immediately followed by a function declaration. That function is what will be executed when the relevant web address is visited.
* The `send_file()` function will look for the named file in your project root and send it to the web browser.

## Receiving form data

Web servers receive the information a user types into the forms on webpages. They then process that data and decide what to do with it, and generate some kind of response to send to the user. This is a basic example of receiving data from web form. As an added bonus I've included a couple of extras:

* The redirect will allow you to send the user to a different page (see the return statement)
* The session variable is a dictionary that Python keeps that is unique to each individual person visiting your web site. You can use it to store information about who they are, so you can reference it next time they visit.

In `main.py`:

```python
@app.route("/demo2", methods=["POST"])
def demo2():
    uid = request.form["userid"]
    pwd = request.form["passwd"]
    print("You have tried to login with username {0} and password {1}".format(uid,pwd))
    session["username"] = uid
    return redirect("/")
```

In file `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<body>
    <form action="/demo2" method="post">
        Userid: <input type="text" name="userid" value=""><br>
        Passwd: <input type="text" name="passwd" value=""><br>
        <input type="submit" name="submit" value="Login">
    </form>
</body>
</html>
```

The following information is available from the request object:

* request.args ... the arguments passed via a url (ie: the bit after the ? in a get)
* request.form ... data passed via a form post (like the above example)
* request.values ... this is .args and .form combined
* request.files ... any files uploaded? see next heading for how to use this
* request.json ... check the .is_json() or the .mimetype to tell if this is set
* request.headers
* request.cookies
* request.authorization
* request.method ... eg: GET or POST
* request.remote_user
* request.user_agent ... what web browser are they using?
* request.mimetype

## File uploads

A rather common task is to have the user upload a file to the web server. Fortunately Flask makes it really easy.

* To use this example, create a photos/ folder in your project root.

```python
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'doc', 'docx'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#...
#... skipping to the good bit...
#...
@app.route("/photo", methods=["POST"])
def upload_photo():
    # The dictionary key here will be the value of the name attribute in <input type="file" name="file">.
    f = request.files['file']  
    # secure_filename protects you from security risks associated with using a user-supplied filename.
    f.save(os.path.join(app.root_path, 'photos', secure_filename(f.filename)))
    return 'file uploaded successfully'
```

With the following HTML

```html
<!DOCTYPE html>
<html lang="en">
<body>
    <form action="/photo" method="POST" enctype="multipart/form-data">
        <input type="file" capture="camera" accept="image/*" name="file"><br>
        <input type="submit" value="Upload!">
    </form>
</body>
</html>
```

## Using a HTML template

Flask uses a template language called Jinja2.

The purpose of the template is it will allow you to create HTML files (or, I guess, CSS/Javascript files) that have parts of their contents automatically replaced with values stored in your Python variables. For instance: It can loop through lists, to automatically create visually appearing forms and lists of information.

Flask expects that files to be used as templates are stored in a templates/ folder in project root. It will automatically look in that folder.

A simple route that processes and returns the result of a template might look like this:

```python
from flask import render_template

@app.route("/demo")
def demo():
    list = []
    list.append({"givenName":"Paul", "familyName":"Baumgarten", "email": "pbaumgarten@isl.ch"})
    list.append({"givenName":"Marty", "familyName":"McFly", "email": "marty@pinheads.com"})
    list.append({"givenName":"Emmett", "familyName":"Brown", "email": "emmett@greatscot.com"})
    return render_template('demo.html', data=list)
```

Where the `templates/demo.html` file looks like:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Contacts list</title>
</head>
<body>
      <table border = 1>
          <thead><tr><td>Given name</td><td>Family name</td><td>Email address</td></tr></thead>
          <tbody>
            {% for person in data %}
                <tr><td> {{ person["givenName"] }} </td><td> {{ person["familyName"] }} </td><td> {{ person["email"] }} </td></tr>
            {% endfor %}
          </tbody>
      </table>
</html>
</body>
</html>
```

I won't go into the template language itself as that would take up too much space. The TutorialsPoint resource linked below is a really useful starting point so that a look at that.

Good overview tutorial:

* https://www.tutorialspoint.com/flask/flask_templates.htm

Official docs:

* http://jinja.pocoo.org/docs/2.10/templates/

## Demo Exercise: Chat app

There is quite a bit of code here!

```python
### File: main.py
from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import send_file
from datetime import datetime
import sqlite3
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'booyeah!secret!'

def database_execute(sql, data):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute(sql, data)
    conn.commit()
    conn.close()

def database_read(sql, data):
    c = sqlite3.connect("chat.db").cursor()
    c.execute(sql, data)
    response = c.fetchall()
    c.close()
    return response

@app.route('/')
def home():
    return send_file("main.html")

@app.route("/message", methods=["POST"])
def upload_message():
    message = request.form["message"]
    displayName = request.remote_addr
    sql = "INSERT INTO messages (time, displayName, message) VALUES (?,?,?)"
    timestamp = int(datetime.now().timestamp())
    database_execute(sql,(timestamp, displayName, message ))
    print("Saved message for {1} (time {0}): {2}".format(timestamp, displayName, message ))
    return 'message received'

@app.route("/messages", methods=["GET","POST"])
def get_message():
    sql = "SELECT * FROM messages ORDER BY time DESC LIMIT 50;"
    messages = database_read(sql, ())
    reply = json.dumps(messages)
    return reply

def initialise_database():
    sql = "CREATE TABLE IF NOT EXISTS messages (time INTEGER, displayName TEXT, message TEXT);"
    database_execute(sql, ())

if __name__ == "__main__":
    initialise_database()
    app.run(host='0.0.0.0', port=8080)
```

In the file `main.html`

```html
<!doctype html>
<html>
    <head></head>
    <style>
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr 5fr;
            grid-column-gap: 1em;
            grid-row-gap: 1em;
            width: 100vw
        }
        .cell { grid-column: span 1; }
    </style>
    <body>
        <div class="grid">
            <span class="cell"><h1>Chat!</h1></span>
            <span class="cell">Send your message:</span>
            <div class="cell">
                <input id="input-message" name="msg" type="text" maxsize="100" size="50" placeholder="Your message here...">
                <input id="input-submit" type="button" value="Send">
            </div>
        </div>
        <div>&nbsp;</div>
        <div class="grid">
            <span class="cell">Date / time</span>
            <span class="cell">Sender</span>
            <span class="cell">Message</span>
        </div>
        <div class="grid" id="messages-destination">
        </div>
    </body>
    <script language="JavaScript" src="/static/main.js"></script>
</html>
```

In the file `static/main.js`

```javascript
"use strict";
function app() {
    function ajax( url, formData, callback ) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (xhttp.readyState === 4) {
                console.log("[ajax] completed: ",xhttp.status,xhttp.responseText)
                if (callback !== null) {
                    callback( xhttp.status, xhttp.responseText );
                }
            }
        };
        xhttp.open("POST", url, true);
        if (formData !== null) {
            xhttp.send(formData);
        } else {
            xhttp.send();
        }
    }

    function sendNewMessage(e) {
        var message = document.querySelector("#input-message").value;
        var form = new FormData();
        form.append('message', document.querySelector("#input-message").value);
        document.querySelector("#input-message").value = "";
        ajax( "/message", form, null );
    }

    function showMessages(status, received) {
        var updates = JSON.parse(received);
        var html = "";
        for (var i in updates) {
            var update = updates[i];
            var d = new Date(Number(update[0])*1000);
            html += "<span class='cell'>"+d.toLocaleString()+"</span>";
            html += "<span class='cell'>"+update[1]+"</span>";
            html += "<span class='cell'>"+update[2].toLocaleString()+"</span>";
        }
        document.getElementById( "messages-destination" ).innerHTML = html;
    }

    function refreshMessages() {
        ajax("/messages", null, showMessages);
    }

    ajax("/messages", null, showMessages);
    document.querySelector("#input-submit").onclick = sendNewMessage;
    setInterval(refreshMessages,2000);
}
window.onload=app;
```

## Flask sessions

The last section to mention with Flask is the idea of a "session". A session is effectively a dictionary object you can use to store key-values about a person browsing your website. It is so named, as (generally) once they close their browser window, their "session" has ended and the data is lost. Sessions are a commonly used way to keep track of the username of someone who has logged into your website, without having to obtain and re-verify their password on every page laod.

The quickest and easiest session system to setup uses the filesystem to store the data you assign. Later on, you'll want to learn how to use databases for this.

```python
# Additional Flask includes for sessions
from flask import session
from flask_session import Session

# Config settings for the session
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(app.root_path, "cache") # Store session data in a /cache folder
app.config['SESSION_FILE_THRESHOLD'] = 1000 # Allow up to 1000 sessions
Session(app)

@app.route('/')
def home():
    session["last_accessed"] = datetime.now()
    return "Welcome"

@app.rout('/when_was_i_last_here')
def lasthere():
    return "You were last here {}".format(session["last_accessed"])
```
