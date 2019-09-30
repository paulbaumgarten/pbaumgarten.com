# Google Firebase

Google Firebase is one of a number of tools that Google makes available for developers. It is quite handy as a "proof of concept" tool that minimises the need for you to create your own "back end" server.

Firebase can be used to provide:

* Authentication of users against their pre-existing Google credentials.
* Store/retrieve application data in JSON format
* Upload/download files for storage 

Firebase provides a "free tier" of use that makes it especially handy for use in class with students. That said, "real world" project really should be moved off firebase to your own backend system prior to lauch, as case studies show it can very quickly get considerably more expensive to use Firebase when compared to maintaining your own infrastructure.

There are also other solutions available that provide a similar service to Firebase. Some of the more common ones include Parse (a Facebook product), MongoDB (a commerial no-sql database that is also available on an open-source license), CouchDB+PouchDB (an open source product led by the Apache foundation), and Kinto (another open source product with it's own foundation). 

To illustrate how Firebase works, we'll create a couple of demo projects.

* **Authdemo** - will walk you through creating your first Firebase project, and to get it working with the authentication system - something that basically any other Firebase project will require. You will re-use 99% of this code in the later projects so I would encourage you to do this without skipping. An online demo of this is available at [https://authdemo.jigsawapps.net](https://authdemo.jigsawapps.net).

* **Notekeeper without attachments** - A simple notes app where the user logs in with their Google account and can read/write notes that are private to them. This will explain how to use the Firebase database.

* **Notekeeper full** - We extend the previous Notekeeper app to include uploading of attachment files to individual notes. An online demo of this is available at [https://notekeeper.jigsawapps.net](https://notekeeper.jigsawapps.net).

These notes have been prepared and tested on Firebase v5.4.1. Firebase changes it's SDK libraries frequently, often in ways that "break" old code. If you are using a version newer than this (particularly if it is v6 or higher) it is likely some of these instructions will be out of date.

<div class="page"/>

# 5.1 - Firebase authentication

See a demo of this project running at [https://authdemo.jigsawapps.net/](https://authdemo.jigsawapps.net/)

## Start a Firebase project

* Create a new Firebase project @ https://console.firebase.google.com
* Goto Develop / Authentication / Users / Setup sign-in method
* Scroll to "Google" and turn on "enable"
  * Make note of your project public-facing name: eg `project-0000000000`
  * Provide a project support email.
  * Make note of your Web SKD configuration. You need your web client ID (eg `00000000000-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com`) and web client secret (eg `Ab1Cd2Ef4Gh5Ij6Kl7`).
* Scroll to Authorised domains
  * Add the domain that you will be hosting your project from eg: `mysuperproject.com` (you can add this later if you are not sure what it will be at the start)
* On the main sidebar, click on "Project Overview". On the "Get started by adding Firebase to your app" page, click on the `</>` icon and copy the code section that appears into your HTML header as shown in the HTML code sample on the next page in the section labelled `<-- Initialise Firebase -->`.

## Run a webserver on localhost

You will need a "webserver" to run on your computer. This will allow you to open your project files using "http://localhost" or similar in your webbrowser, as if it was on a real website.

Check my website for the current suggested solution to this at https://pbaumgarten.com/javascript

The rest of this exercise assumes you have a webserver running on localhost.

## The demo explained

The HTML is relatively straight forward. In the header we are loading the various scripts that provide Firebase functionality, and providing our individualised configuration settings. Within the body, there are three main `<div>` tags, of `unknown`, `signed-out` and `signed-in`. Each of these will turn green when they represent the current state of authentication.

The Javascript code is based upon the sample provided in the Firebase documents, but I've modified it slightly to make it simpler for students to "drop into" their projects. It has been written in such as way as you can copy-and-paste the `toggleSignIn()` and `requireSignIn()` functions into any project and, subject to the conditions below, it will "just work".  Those conditions are:

* `toggleSignIn()` should be run anytime you want to initiate a log-in or log-out with the users Google account. Typically this means you would use a "sign in/out button" event handler to call it. You can see this occurring in the last line of `main()`.
* `window.onload = requireSignIn;` will obtain the current sign-in/out status prior to running any other Javascript. It does not restrict your page doing other things, but this should always be the first function run. You still put your program code in `main()`.
* There must be a `main()` function that accepts two parameters. In the demo, you will see I called them `status` and `userData`. The `requireSignIn()` function will execute `main()` everytime the sign-in/out status changes.  There are three possible status values: `unknown`, `signed-in` and `signed-out`. You should run your program checking these and behaving accordingly (as seen in the `if` statement within `main()`).
* When the status is set to `signed-in`, the second parameter (`userData` in the example) will contain a JSON object with information about the person who has signed in. These properties are: `.displayName`, `.email`, `.emailVerified`, `.photoURL`, `.isAnonymous`, `.uid`, and `.providerData`.

The intention behind structuring these functions this way is so you can create your app based on your `main()` function and simply check the status and userData variables to decide what to do and are able to trust that the authentication is all working.

![](img/authdemo.png)

<div class="page"/>

```html
<!doctype html>
<html>
    <head>
        <title>Notekeeper</title>
        <link rel="stylesheet" href="my-project.css">

        <!-- Firebase App is always required and must be first -->
        <script src="https://www.gstatic.com/firebasejs/5.4.1/firebase-app.js"></script>
        <script src="https://www.gstatic.com/firebasejs/5.4.1/firebase-auth.js"></script>
        <script src="https://www.gstatic.com/firebasejs/5.4.1/firebase-database.js"></script>
        <script src="https://www.gstatic.com/firebasejs/5.4.1/firebase-storage.js"></script>

        <!-- Initialize Firebase -->
        <script>
        var config = {
            apiKey: "---your apikey goes here---",
            authDomain: "---your auth domain goes here---",
            databaseURL: "---your database url goes here---",
            projectId: "---your project id goes here---",
            storageBucket: "---your storage bucket goes here---",
            messagingSenderId: "---your messaging sender id goes here---"
        };
        firebase.initializeApp(config);
        </script>

        <!-- Your project code -->
        <script type="text/javascript" src="my-project.js"></script>
    </head>
    <body>
        <div >
            <h1>Authentication Demo</h1>
            <p>This demo uses <a href="https://firebase.google.com">Google Firebase</a> version 5.4.1</p>
        </div>
        <div id="unknown">
            <p>Sign in status is unknown / being determined</p>
        </div>
        <div id="signed-out">
            <p>You must be signed in with your Google account to use this app.</p>
        </div>
        <div id="signed-in">
            <p>You are successfully signed in!</p>
            <p>Display name: <span id="display-name"></span></p>
            <p>Email address: <span id="email"></span></p>
            <p>Photo: <img id="photo" src=""></span></p>
        </div>
        <div>
            <p><input type="button" id="sign-in-button" value="Sign in/out with Google"></p>
        </div>
    </body>
</html>
```

<div class="page"/>

```js
"use strict;"

function toggleSignIn() {
    if (!firebase.auth().currentUser) {
        let provider = new firebase.auth.GoogleAuthProvider();
        provider.addScope('email');
        firebase.auth().signInWithRedirect(provider);
    } else {
        firebase.auth().signOut();
    }
}

function requireSignIn() {
    let account = {};
    firebase.auth().getRedirectResult().then(function(result) {
        if (result.credential) {
            account.token = result.credential.accessToken;
            console.log("[requireSignIn] token = ",token)
        }
        let user = result.user;
    }).catch(function(error) {
        let errorCode = error.code;
        let errorMessage = error.message;
        let email = error.email;
        let credential = error.credential;
        console.log("[requireSignIn] error = ",error);
        if (errorCode === 'auth/account-exists-with-different-credential') {
            alert('You have already signed up with a different auth provider for that email.');
        }
    });
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            // User is signed in.
            console.log("[requireSignIn] user = ", user);
            account.displayName = user.displayName; 
            account.email = user.email; 
            account.emailVerified = user.emailVerifiedl; 
            account.photoURL = user.photoURL; 
            account.isAnonymous = user.isAnonymous;
            account.uid = user.uid;
            account.providerData = user.providerData;
            main("signed-in", account);
        } else {
            // User is signed out.
            main("signed-out", null);
        }
    });
    main("unknown", null);
}

function main(status, userData) {
    console.log(status, userData);
    if (status === "unknown") {
        document.querySelector("#unknown").className = "active";
        document.querySelector("#signed-in").className = "inactive";
        document.querySelector("#signed-out").className = "inactive";
    } else if (status === "signed-out") {
        document.querySelector("#unknown").className = "inactive";
        document.querySelector("#signed-in").className = "inactive";
        document.querySelector("#signed-out").className = "active";
    } else if (status === "signed-in") {
        document.querySelector("#unknown").className = "inactive";
        document.querySelector("#signed-in").className = "active";
        document.querySelector("#signed-out").className = "inactive";
        // Display user information
        document.querySelector("#display-name").innerHTML = userData.displayName;
        document.querySelector("#email").innerHTML = userData.email;
        document.querySelector("#photo").src = userData.photoURL;
    }
    document.querySelector("#sign-in-button").addEventListener("click", toggleSignIn);
}

window.onload = requireSignIn;
```

<div class="page"/>

# 5.2 - Firebase database

See a demo of this project running at [https://notekeeper.jigsawapps.net/](https://notekeeper.jigsawapps.net/)

The final Notekeeper app looks like this. In this exercise we will create the first part which only lacks the file attachment section (we will had that in the next part).

![](img/notekeeper.png)

Functionally, the app behaves as:

* Require the user to sign in with a Google account
* New notes can be created by clicking new note.
* Changes are automatically saved to the Firebase database
* Updates to the database should automatically update the list of notes available in the sidebar

To build this:

* Take a copy of the HTML you used for `AuthDemo`, and replace the contents of `<body>` with that shown below. You'll notice the HTML isn't too fancy, just a bunch of div's being used for layout and styling purposes, and a few text boxes and buttons.
* For the Javascript, again start with a copy of the file you used in `AuthDemo`. Add the new functions and replace the `main()` with those provided.
* Make sure you get the CSS from section 5.4 (I will have a copy of the this CSS file available at [pbaumgarten.com/javascript](https://pbaumgarten.com/javascript) so you don't have to write it all out).

<div class="page"/>

## Understanding the Firebase database

The following outlines how the Firebase database is used in this project.

Note that `account.uid` is just a string that has been provided to us by the authentication system in Firebase. It is a code that we can treat as unique to an individual user, as a way of identifying them.

### Saving to the database

```javascript
firebase.database().ref( "/users/" + account.uid + "/" + _id).set( note );
```

The key to understanding this line are parameters given in the `ref()` and `set()` functions. To re-work it as a generic command, it might look like:  

```javascript
firebase.database().ref( database_location ).set( data_to_save );
``` 

... where `database_location` is a string and `data_to_save` is any Javascript variable including JSON objects or arrays.

Database locations are stored as a tree, with each branch denoted by a forward slash `/`. So, replacing variables for raw strings, the following are some valid examples:

```javascript
firebase.database().ref( "/contacts/john_doe" ).set( { "email": "john@doe.com" } );
firebase.database().ref( "/riddle/1" ).set( "The rain in Spain falls mainly in the plains." );
```

Importantly, `set()` will overwrite any existing data at that location. There is an `update()` function available, or you can retrieve a copy of the data at that location first, manipulate it how you want, and then save back over the top.

### Reading from the database

```javascript
firebase.database().ref( "/users/" + account.uid ).on("value", function(data) {
    if (data.val() != null) {
        // .... etc ....
    }
});
```

Like the function that saved to the database, this starts off the same by requesting a reference to a location in the Firebase database via the `ref()` function and the parameter provided. Instead of invoking `set()`, however, we initialise an event handler named `on()`.

The `on()` event handler will execute the callback function in it's second parameter when it receives data from the database.

One really nice thing about the `on()` function is that it will re-execute anytime new data is available at the reference location. This means your program can automatically process any updates. This is useful for things like chat applications where multiple users might be storing/changing data at a time - it can allow you to have a "live feed" of changes occuring.

If you only want the data to be retrieved once and don't care about updates, you can replace the `on()` function with the `once()` function.

The reason for the if statement checking `if (data.val() != null)` is to catch if nothing currently exists at the location we asked for. Typically, this might mean we want an `else` that will provide the default values to our program if the data doesn't exist.

### Deleting from the database

```javascript
firebase.database().ref( "/users/" + account.uid + "/" + _id).remove();
```

By now this should hopefully be familiar. This function obtains a reference to a location in the Firebase database, and simply runs the `remove()` function to delete the data.

<div class="page"/>

```html
<!doctype html>
<body>
    <div id="sign-in-unknown" class="modal">
        <p>Verifying your account status...</p>
    </div>
    <div id="sign-in-required" class="modal">
        <p>You must be signed in with your Google account to use this app.</p>
        <p><input type="button" id="sign-in-button" value="Sign in with Google"></p>
    </div>
    <div id="sign-in-ok" class="layout_wrapper style_wrapper" style="display:none">
        <div class="layout_header style_box">
            <span>Notes for <span id="user_display_name"></span></span>
            <span class="right"><input type="image" id="user_pic" src="">
                <div id="signOutInfoBox">Click to sign out</div>
            </span>
        </div>
        <div class="layout_pages style_box nav">
            <ul id="notelist">
            </ul>
            <input type="button" id="newnote" value="New note">
        </div>
        <div class="layout_note style_box">
            <div>
                <input type="text" id="notetitle" maxlength="30" placeholder="Note title...">
                <input type="hidden" id="noteid" value="0">
            </div>
            <div><textarea id="notecontent" rows="20" placeholder="Note content..."></textarea></div>
            <div id="noteattachments"><p>Attachments:</p><span id="attachments_list"></span><span><input type="file" id="add_attachments" value="Add file(s)"></span></div>
        </div>
        <div class="layout_footer">
            <p><span id="savestatus">Not saved</span> Last updated: <span id="lastupdated">n/a</span> <input type="button" id="deletenote" value="Delete note"></p>
        </div>
    </div><!-- .wrapper -->
</body>
```

<div class="page" />

```js
function uuid4(){
    // Function to generate a randomised number that is compliant with the UUID4 format 
    // (refer to https://en.wikipedia.org/wiki/Universally_unique_identifier)
    var dt = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0;
        dt = Math.floor(dt/16);
        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
    });
    return uuid;
}

function newNote(e) {
    // Generate a random ID for this note
    let _id = uuid4();
    // Display the note on screen
    document.querySelector("#noteid").value = _id;
    document.querySelector("#notetitle").value = "";
    document.querySelector("#notecontent").value = "";
    document.querySelector("#notetitle").style.display = "initial";
    document.querySelector("#notecontent").style.display = "initial";
}

function saveNote(e) {
    let _id = document.querySelector("#noteid").value;
    let note = {
        "content": document.querySelector("#notecontent").value,
        "title": document.querySelector("#notetitle").value,
        "_id": _id
    };
    console.log("[saveNote] putting ",note);
    firebase.database().ref("/users/" + account.uid + "/" + _id).set( note );
}

function noteChanged(e) {
    document.querySelector("#savestatus").className = "unhealthy";
    document.querySelector("#savestatus").innerHTML = "Changes not saved";
}

function deleteNote(e) {
    if (window.confirm("Delete note?")) {
        let _id = document.querySelector("#noteid").value;
        // Delete note from server
        firebase.database().ref( "/users/" + account.uid + "/" + _id).remove();
        // Clear the note content from screen
        document.querySelector("#notetitle").style.display = "none";
        document.querySelector("#notecontent").style.display = "none";
    }
}

function displayNote(e) {
    let _id = e.target.dataset.noteid;
    // Ensure the note fields are visible
    document.querySelector("#notetitle").style.display = "initial";
    document.querySelector("#notecontent").style.display = "initial";
    // Set the content of the note
    document.querySelector("#notetitle").value = notes[_id].title;
    document.querySelector("#notecontent").value = notes[_id].content;
    document.querySelector("#noteid").value = _id;
}

function displayNotesList(notes) {
    let html = "";
    for (let i in notes) {
        html = html + "<li class='displayNoteLink' data-noteid='"+notes[i]._id+"'>"+notes[i].title+"&nbsp;</li>\n";
    }
    document.querySelector("#notelist").innerHTML = html;
    let elements = document.querySelectorAll(".displayNoteLink");
    for (let element of elements) {
        element.addEventListener("click", displayNote);
    }
}

function getNotesFromStorage() {
    firebase.database().ref( "/users/" + account.uid ).on("value", function(data) {
        console.log("[getNotesFromStorage] received = ",data.val());
        if (data.val() != null) {
            notes = data.val();
            displayNotesList(notes);
        }
        document.querySelector("#savestatus").className = "healthy";
        document.querySelector("#savestatus").innerHTML = "All saved";
    });
}

function toggleSignOutInfoBox(e) {
    if (e.type=="mouseover") {
        document.querySelector("#signOutInfoBox").style.display = "block";
    } else {
        document.querySelector("#signOutInfoBox").style.display = "none";
    }
}

function main(status, userInfoProvided) {
    if (status === "unknown") {
        document.querySelector("#sign-in-unknown").style.display = "block";
        document.querySelector("#sign-in-ok").style.display = "none";
        document.querySelector("#sign-in-required").style.display = "none";
    } else if (status === "signed-out") {
        document.querySelector("#sign-in-unknown").style.display = "none";
        document.querySelector("#sign-in-ok").style.display = "none";
        document.querySelector("#sign-in-required").style.display = "block";
        document.querySelector("#sign-in-button").addEventListener("click", toggleSignIn);
    } else if (status === "signed-in") {
        account = userInfoProvided;
        document.querySelector("#sign-in-unknown").style.display = "none";
        document.querySelector("#sign-in-ok").style.display = "grid";
        document.querySelector("#sign-in-required").style.display = "none";
        // Load existing notes (if any)
        getNotesFromStorage();
        // Event handlers
        document.querySelector("#newnote").addEventListener("click", newNote);
        document.querySelector("#deletenote").addEventListener("click", deleteNote);
        document.querySelector("#notetitle").addEventListener("change", saveNote);
        document.querySelector("#notecontent").addEventListener("change", saveNote);
        document.querySelector("#notetitle").addEventListener("input", noteChanged);
        document.querySelector("#notecontent").addEventListener("input", noteChanged);
        document.querySelector("#user_pic").addEventListener("click", toggleSignIn);
        document.querySelector("#user_pic").addEventListener("mouseover", toggleSignOutInfoBox);
        document.querySelector("#user_pic").addEventListener("mouseout", toggleSignOutInfoBox);
        // Hide the note title and content until either a new note is requested, or an existing is requested for loading.
        document.querySelector("#notetitle").style.display = "none";
        document.querySelector("#notecontent").style.display = "none";
        // Display user information
        document.querySelector("#user_pic").src = account.photoURL;
        document.querySelector("#user_display_name").innerHTML = account.displayName + " ("+account.email+")";
    }
}
```

<div class="page"/>

# 5.3 - Firebase file storage

## Understanding Firebase file storage

### Uploading a file

```javascript
let reference = firebase.storage().ref().child( account.uid + "/" + f.name );
reference.put( f ).then(function(snapshot) {
    console.log("User "+account.uid+" ("+account.email+") has uploaded file "+f.name);
}
```

While the syntax initially looks similar to using the Firebase database there are crucial differences to note. For instance, the folder+file location is being provided as a parameter to the `child()` function rather than `ref()`.  Similar to the database, however, this is a slash separated folder and file location. For instance `.child( "myfolder/myfile.jpg" )` would be valid. 

Then to upload, you call the `put()` function attached to the reference variable you just created, passing the file object as the parameter. For more information on creating those file objects, check the earlier section for uploading a file with a form. As a quick recap, you can create a file upload in HTML and Javascript using the following.

```html
<input type="file" id="file_upload_button">
```

```javascript
document.querySelector("#file_upload_button").addEventListener("change", uploadFile);

function uploadFile(e) {
    let file_to_put = this.files[0];
    // I can now use firebase's "put( file_to_put )"
}
```

### Downloading a file

```javascript
let reference = firebase.storage().ref().child( account.uid + "/" + item );
reference.getDownloadURL().then(function (url) {
    span.innerHTML += "<a href='"+url+"' target='_blank'>"+item+"</a><br>\n";
});
```

### Obtaining a list of files

Nup. Can't do it. Firebase doesn't have a function to give you a list of the files you've uploaded. Because of this, it is generally a good idea to record the names of uploaded files in your database somewhere, so you can extract them later. That's what the `filesList` is doing in the attachment functions below.

<div class="page"/>

## Finishing the Notekeeper project

```js
function displayNote(e) {
    /**
     * .... all code unchanged
     * .... add the following at the end of the function
     */ 

    // Show attachments list
    document.querySelector("#noteattachments").style.display = "initial"; // < ------ INSERT
    attachmentsDisplay();       // < ------- INSERT
}

function attachmentUpload(e) {
    // Get the file information from the <input type='file'> element
    let f = this.files[0];
    console.log("[attachmentUpload] uploading "+f.name);
    // Upload the file
    let reference = firebase.storage().ref().child( account.uid + "/" + f.name );
    // This line does the actual upload
    reference.put( f ).then(function(snapshot) {
        console.log("User "+account.uid+" ("+account.email+") has uploaded file "+f.name);
        /* 
        While the file is now uploaded, Firebase does not provide us a list of all our files. 
        We have to maintain our own list in the database, hence the following code fragment. 
        */
        let _id = document.querySelector("#noteid").value;
        // Retrieve list of files already attached to this note
        let filesList = firebase.database().ref("/users/" + account.uid + "/" + _id + "/files");
        // Once we receive the list of files,
        filesList.once("value").then(function(data) {
            // Save a reference to the file in the database so we can access it later
            list = data.val() || [];// if no currently no files, set list to an empty array
            list.push( f.name );    // Add our filename to the list of files
            filesList.set( list );  // Save the list to firebase database
            attachmentsDisplay();   // Update the visible list of attachments
        });
    });
}

function attachmentsDisplay() {
    let _id = document.querySelector("#noteid").value;
    let span = document.querySelector("#attachments_list");
    span.innerHTML = "";
    // Get the list of files
    let filesList = firebase.database().ref("/users/" + account.uid + "/" + _id + "/files");
    filesList.once("value").then(function(data) {
        list = data.val() || [];// if no currently no files, set list to an empty array
        for (let item of list) {
            let reference = firebase.storage().ref().child( account.uid + "/" + item );
            reference.getDownloadURL().then(function (url){
                span.innerHTML += "<a href='"+url+"' target='_blank'>"+item+"</a><br>\n";
            });
        }
    });
}

function main(status, userInfoProvided) {
    /**
     * .... all this code unchanged
     */ 
    } else if (status === "signed-in") {
    /**
     * .... all code unchanged
     * .... add the following within this 'else if' block
     */ 

        // Add attachments items
        document.querySelector("#noteattachments").style.display = "none";
        document.querySelector("#add_attachments").addEventListener("change", attachmentUpload);
        attachmentsDisplay();
    }
}

window.onload = requireSignIn;
```

<div class="page"/>

Find the `<div class="layout_note style_box">` section of your **Notekeeper** HTML and modify it to add the `<div>` with `id=noteattachments` and it's contents:

```html
    <div class="layout_note style_box">
        <div>
            <input type="text" id="notetitle" maxlength="30" placeholder="Note title...">
            <input type="hidden" id="noteid" value="0">
        </div>
        <div><textarea id="notecontent" rows="20" placeholder="Note content..."></textarea></div>
        <div id="noteattachments">
            <p>Attachments:</p>
            <span id="attachments_list"></span>
            <span><input type="file" id="add_attachments" value="Add file(s)"></span>
        </div>
    </div>
```

<div class="page"/>

# 5.4 - CSS for Firebase projects

All projects in this chapter use the following CSS in `my-project.css`:

```css
html, body {
    padding: 0 0 0 0;
    margin: 0 0 0 0;
    background: #fff;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
}

/* Default layout for mobile devices */
.layout_wrapper {
    display: grid;
    grid-gap: 10px;
    grid-template-areas:
    "header"
    "pages"
    "note"
    "footer"
}

/* Layout for greater than 900 pixel wide devices */
@media only screen and (min-width: 900px) and (orientation:landscape)  {
    .layout_wrapper {
        grid-gap: 10px;
        grid-template-columns: 200px auto;
        grid-template-areas:
        "header header"
        "pages note"
        "pages footer";
    }
}

.layout_header {    grid-area: header;  }
.layout_pages {     grid-area: pages;  }
.layout_note {      grid-area: note;  }
.layout_footer {    grid-area: footer;  }

/* Optional styling code just to help illustrate the grid effect */
.style_wrapper {
    background-color: #fff;
    color: #444;
    margin: 10px;
}

/* Optional styling code just to help illustrate the grid effect */
.style_box {
    background-color: #d0d0d0;
    color: #000000;
    border-radius: 5px;
    padding: 10px;
}

input[type=text],input[type=password] {
    width: 90%;
    padding: 2%;
    margin: 2%;
    font-size: 12pt;
    box-sizing: border-box;
    border: 2px solid #b0b0b0;
    border-radius: 4px;
}

#layout_note {
    min-height: 400px;
}

textarea#notecontent {
    width: 90%;
    height: 90%;
    padding: 2%;
    margin: 2%;
    font-size: 12pt;
    box-sizing: border-box;
    border: 2px solid #b0b0b0;
    border-radius: 4px;
}

.nav ul {
    list-style: none;
    margin: 0;
    padding-left: 0;
}

.nav li {
    display: block;
    position: relative;
    text-decoration: none;
    transition-duration: 0.5s;
    border: 1px solid #808080;
    border-radius: 3px;
    margin: 5px;
    background-color: #d0d0d0;
}

.nav li:hover {
    background-color: #a0a0a0;
    cursor: pointer;
}

.nav a {
    text-decoration: none;
    color: #000000;
    padding: 2px;
    border: 1px solid #c0c0c0;
    border-radius: 3px;
}

input[type=button],input[type=file] {
    padding: 10px;
    border-radius: 10px;
    margin: 3px;
    background-color: #0000ff;
    color: #ffffff;
    font-size: 12pt;
}

input[type=button]:hover, input[type=file]:hover {
    background-color: #000080;
}

.unhealthy {
    font-weight: bold;
    color: #a00000;
}

.healthy {
    font-weight: bold;
    color: #00a000;
}

.modal {
    position: fixed;
    padding: 20px 20px 20px 20px;
    top: 25vh;
    left: 30vw;
    width: 40vw;
    height: 40vh;
    background-color: #ffffff;
    border: 2px solid #3333dd;
    border-radius: 10px;
}

#user_pic {
    max-width: 48px;
    max-height: 48px;
    border-radius: 24px;
}

.right {
    float: right;
}

#signOutInfoBox {
    position: absolute;
    z-index: 2;
    border: 1px solid black;
    background-color: red;
    color: white;
    border-radius: 5px;
    padding: 5px;
    display: none;

.active {
    padding: 20px 20px 20px 20px;
    width: 400px;
    background-color: #c0ffc0;
    border: 5px solid #008000;
    border-radius: 10px;
}

.inactive {
    padding: 20px 20px 20px 20px;
    width: 400px;
    background-color: #ffc0c0;
    border: 5px solid #800000;
    border-radius: 10px;
}

#photo {
    max-width: 96px;
    max-height: 96px;
    border-radius: 48px;
}

}
```
