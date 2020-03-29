# Using Google API to authenticate uses in Flask

## Install

```bash
pip install -r requirements.txt
```

Where your requirements.txt contains...

```text
google-api-python-client
google-auth
google-auth-oauthlib
google-auth-httplib2
```

## Imports

```python
from flask_session import Session               ## pip install Flask-Session
import google.oauth2.credentials                ## Used by Google OAuth
import google_auth_oauthlib.flow                ## Used by Google OAuth
from googleapiclient.discovery import build     ## Used by Google OAuth
```

## Global code

 * Ensure your sessions system is up and running. The following example just uses the local filesystem instead of a database

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'esdirolftjg rdsklthjrm,gme jkm2mw,3 werkj hswedf kdsjkh'
app.config['SESSION_TYPE'] = "filesystem"
app.config['SESSION_FILE_DIR'] = os.path.join(app.root_path, "sessions")
app.config['SESSION_FILE_THRESHOLD'] = 1000
Session(app)
```

 * Set the location of your client_secrets.json file and your Google Scopes

A list of the various scopes is available at [https://developers.google.com/identity/protocols/oauth2/scopes](https://developers.google.com/identity/protocols/oauth2/scopes)

The client_secrets.json file should not be in your project folder. This is generally considered insecure practice. It is also recommended to not hardcode the location of your secrets file, but to set it via an environment variable.

```python
CLIENT_SECRETS_FILE = '../client_secret.json' # ... OR ...
CLIENT_SECRETS_FILE = os.environ['client_secrets']
SCOPES = ['https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        "openid"]
```

## Setting environment variables

Via nginx

```
location / {
    uwsgi_param     CLIENT_SECRETS_FILE     '/folder/folder/client_secrets.json';
}
```

Ubuntu

* Add to `/etc/environment` (note: a reboot will be required)


## Routes

```python
@app.route("/")
def main():
    if "credentials" not in session:    ## If not logged in
        return redirect("authorize")    ## Start the login process
    elif "user" in session:             ## If we are logged in
                                        ## Return a customised index page
        return render_template("index.html", person=session['user']['name'])
    else:                               ## Else
        return send_file("index.html")  ## This should never be reached?

## Used by Google OAuth
def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes,
            'id_token': credentials.id_token}

## Used by Google OAuth
@app.route("/login")
def login():
    if "credentials" not in session:
        return redirect("authorize")
    else:
        return redirect("/")

## Used by Google OAuth
@app.route("/authorize")
def authorize():
    # Intiiate login request
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    return redirect(authorization_url)

## Used by Google OAuth
@app.route("/oauth2callback")
def oauth2callback():
    # Receive an authorisation code from google
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_response = request.url
    # Use authorisation code to request credentials from Google
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)
    # Use the credentials to obtain user information and save it to the session
    oauth2_client = build('oauth2','v2',credentials=credentials)
    user_info= oauth2_client.userinfo().get().execute()
    session['user'] = user_info
    # Return to main page
    return redirect(url_for('/'))
```

## While developing...

* Set OS environment variable `OAUTHLIB_INSECURE_TRANSPORT` to `1` so Google will allow http
* Set the app.run parameter `debug=True`

```python
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.run(host="0.0.0.0", port=8080, debug=True)
```

## Session data

An example of the content that will be loaded into `session['user]` by the above process is...

```python
{
    'email':        'myemail@address.com',
    'family_name':  'Baumgarten',
    'given_name':   'Paul',
    'id':           '00000000000000000000',
    'locale':       'en-GB',
    'name':         'Paul Baumgarten',
    'picture':      'https://lh3.googleusercontent.com/a-/AOh14Ggq2pny3unXgESG-LNuy0n_6ZJuCECaCV76k_8H-0Y',
    'verified_email': True
}
```

## See also

* https://developers.google.com/identity/protocols/oauth2/web-server
* https://developers.google.com/identity/protocols/oauth2/scopes
* https://google-api-client-libraries.appspot.com/documentation/oauth2/v2/python/latest/oauth2_v2.userinfo.html

