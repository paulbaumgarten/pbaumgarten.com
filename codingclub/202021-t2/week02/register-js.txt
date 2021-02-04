
function runChecks(event) {
    let userName = document.querySelector("[name='userid']").value;
    let displayName = document.querySelector("[name='displayName']").value;
    let email = document.querySelector("[name='email']").value;
    let password = document.querySelector("[name='password']").value;
    let password2 = document.querySelector("[name='password2']").value;
    if (userName.length == 0) {
        alert("Username can not be empty! You numpty!");
        event.preventDefault()
    }    
    if (displayName.length == 0) {
        alert("Display name can not be empty! You numpty!");
        event.preventDefault()
    }    
    if (email.length == 0) {
        alert("Email address can not be empty! You numpty!");
        event.preventDefault()
    }    
    if (password.length == 0) {
        alert("Password can not be empty! You numpty!");
        event.preventDefault()
    }
    if (password != password2) {
        alert("Passwords do not match! You numpty!");
        event.preventDefault()
    }
}

document.querySelector('#registrationForm').onsubmit = runChecks;
