# Tkinter GUI

## Exercise 1 - Welcome screen

![]("img/tkinter-hello.png")

```python
from tkinter import *

def button_click(text, label):
    name = text.get()
    label["text"] = "Hello "+name+"! Nice to meet you!"

def menu_file_exit():
    exit()

def draw_screen():
    # Create the main program and window
    window = Toplevel()
    window.geometry("500x200")
    window.title("My first window program")
    # Create the main menu bar
    menu = Menu(window)
    window.config(menu=menu)
    # Create a sub menu for File
    menu_file = Menu(menu)
    menu_file.add_command(label="New")
    menu_file.add_command(label="Save")
    menu_file.add_command(label="Quit", command=menu_file_exit)
    menu.add_cascade(label="File", menu=menu_file)
    # Create a sub menu for Help
    menu_help = Menu(menu)
    menu_help.add_command(label="About")
    menu.add_cascade(label="Help", menu=menu_help)
    # Create a label
    label1 = Label(text="Please enter your name")
    label1.place(x=20, y=20)
    # Create a text box (called an Entry in TKinter)
    text = Entry(window)
    text.place(x=20, y=50)
    text.focus() # Put the cursor in the text box
    # Create another label
    label2 = Label(window, text="", font=("Helvetica", "24"))
    label2.place(x=20, y=110
    # Create a button
    button = Button(window, text="Hello", command=lambda: button_click(text, label2))
    button.place(x=20, y=80)
    # Finish function
    return window

root = Tk()
windowMainScreen = draw_screen()
root.withdraw() # Hide the root window, work with TopLevel windows instead
root.mainloop()
```

<div class="page"/>

## Exercise 2 - Contacts directory

![]("img/tkinter-contacts.png")

```python
from tkinter import *

contacts = []
contacts.append({"givenName":"Paul", "familyName":"Baumgarten", "email": "pbaumgarten@isl.ch", "phone": "555-0000"})
contacts.append({"givenName":"Emmett", "familyName":"Brown", "email": "emmett@greatscot.com", "phone": "555-0001"})
contacts.append({"givenName":"Marty", "familyName":"McFly", "email": "marty@pinheads.com", "phone": "555-0002"})
contacts.append({"givenName":"Biff", "familyName":"Tannen", "email": "biff@fertilisers-r-us.com", "phone": "555-0003"})
previously_selected = -1 # Start of program use -1

def menu_file_exit():
    exit()

# Create the main program and window
def draw_screen():
    def new_contact():
        global contacts
        contacts.append({"givenName": "New contact", "familyName": "", "email": "", "phone": ""})
        listbox.insert(END, "** New **")
        listbox.select_set(len(contacts) - 1)

    def list_click(e):
        global previously_selected
        # Save changes to previous contact before moving to next
        if previously_selected >= 0:
            this_contact = contacts[previously_selected]

            # Update our entry in the contacts list
            this_contact["givenName"] = text_given_name.get()
            this_contact["familyName"] = text_family_name.get()
            this_contact["email"] = text_email.get()
            this_contact["phone"] = text_phone.get()
            # Update the listing in the list box
            listbox.delete(previously_selected)
            listbox.insert(previously_selected, this_contact["familyName"] + ", " + this_contact["givenName"])

        # Find the selected item in the list
        selected = int(listbox.curselection()[0])  # item number selected in list
        this_contact = contacts[selected]

        # Show the contacts details
        text_given_name.delete(0, END)
        text_given_name.insert(END, this_contact["givenName"])
        text_family_name.delete(0, END)
        text_family_name.insert(END, this_contact["familyName"])
        text_email.delete(0, END)
        text_email.insert(END, this_contact["email"])
        text_phone.delete(0, END)
        text_phone.insert(END, this_contact["phone"])
        # Save this value for next time
        previously_selected = selected

    window = Toplevel()
    window.geometry("550x400")
    window.title("Contacts directory")

    # Create a list
    listbox = Listbox(window, width=20, height=20) # width is characters, height is lines
    for item in contacts:
        listbox.insert(END, item["familyName"]+", "+item["givenName"])
    listbox.place(x=20, y=20)
    listbox.bind('<<ListboxSelect>>', list_click)

    # Create the main menu bar
    menu = Menu(window)
    window.config(menu=menu)

    # Create a sub menu for File
    menu_file = Menu(menu)
    menu_file.add_command(label="New", command=new_contact)
    menu_file.add_command(label="Quit", command=menu_file_exit)
    menu.add_cascade(label="File", menu=menu_file)

    # Create a sub menu for Help
    menu_help = Menu(menu)
    menu_help.add_command(label="About")
    menu.add_cascade(label="Help", menu=menu_help)

    # Create labels
    label1 = Label(window, text="Given name")
    label1.place(x=220, y=20)
    label1 = Label(window, text="Family name")
    label1.place(x=220, y=50)
    label1 = Label(window, text="Email")
    label1.place(x=220, y=80)
    label1 = Label(window, text="Phone")
    label1.place(x=220, y=110)

    # Create text boxes
    text_given_name = Entry(window)
    text_given_name.place(x=320, y=20)
    text_family_name = Entry(window)
    text_family_name.place(x=320, y=50)
    text_email = Entry(window)
    text_email.place(x=320, y=80)
    text_phone = Entry(window)
    text_phone.place(x=320, y=110)

    return window

# Run the program
window = Tk()
windowMainScreen = draw_screen()
window.withdraw() # Hide the root window, work with TopLevel windows instead
window.mainloop()
```

<div class="page"/>

## Exercise 3 - Chat client

![]("img/tkinter-chat.png")

```python
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from datetime import  datetime
import requests
import os
from PIL import Image, ImageTk

displayName = "---not-set---"
messages = []

def drawMainScreen(width, height, title):

    def send_message():
        print(window)
        messagebox.showinfo("Hmmm...", "Insert code to send message here....")
        this_message = text_message.get()
        messages.append({"from": displayName, "to": "Luke Skywalker", "datetime": datetime.now().timestamp(), "message": this_message})
        print("The message was: ",this_message)
        text_message.delete(0, END)
        displayMessages(messagesList)
        pass

    def new_contact():
        pass

    def menu_file_exit():
        exit()

    def sign_in():
        drawLoginScreen()

    def status_changed(val):
        print("Your status is now: ",val)

    def displayMessages(messagesList):
        messagesList.delete(0, END)
        for item in messages:
            messagesList.insert(END, item["from"] + ", says: " + item["message"])

    window = Toplevel()
    window.title(title)
    dimensions = str(width)+"x"+str(height)
    window.geometry(dimensions)

    messagesList = Listbox(window, width=75, height=20) # width is characters, height is lines
    displayMessages(messagesList)
    messagesList.place(x=20, y=20)

    # Create the main menu bar
    menu = Menu(window)
    window.config(menu=menu)

    # Create a sub menu for File
    menu_file = Menu(menu)
    menu_file.add_command(label="Sign in", command=sign_in)
    menu_file.add_command(label="New", command=new_contact)
    menu_file.add_command(label="Quit", command=menu_file_exit)
    menu.add_cascade(label="File", menu=menu_file)

    # Create a sub menu for Help
    menu_help = Menu(menu)
    menu_help.add_command(label="About")
    menu.add_cascade(label="Help", menu=menu_help)

    # Create labels
    Label(window, text="New message").place(x=20, y=340)

    # Create text boxes
    text_message = Entry(window, width=75)
    text_message.place(x=20, y=360)

    Button(window, text="Send", height=2, command=lambda: send_message()).place(x=500, y=340)

    # Display logo
    img = Image.open("bookface.png").resize((50, 50))
    logo_image = ImageTk.PhotoImage(img)
    logo_label = Label(window, image=logo_image)
    logo_label.image = logo_image
    logo_label.place(x=485, y=20)

    # Status drop down
    status_var = StringVar(root)
    status_var.set("Online") # default value
    status_options = ["Online","Away","Offline"]
    status = OptionMenu(root, status_var, *status_options, command=status_changed)
    status.place(x=485, y=90)

    return window

def drawLoginScreen():
    def do_login():
        login(username=text_username.get(), password=text_password.get(), address=text_address.get())
        window.destroy()

    window = Toplevel()
    window.title("Connect to server")
    window.geometry("400x400")
    Label(window, text="Username").place(x=20, y=20)
    Label(window, text="Password").place(x=20, y=60)
    Label(window, text="Server address").place(x=20, y=100)
    text_username = Entry(window, width=25)
    text_username.place(x=120, y=20)
    text_password = Entry(window, show="*", width=25)
    text_password.place(x=120, y=60)
    text_address = Entry(window, width=25)
    text_address.place(x=120, y=100)
    Button(window, text="Login", height=2, command=do_login).place(x=120, y=140)
    return window

def login(username, password, address):
    global displayName
    print("Connecting to {} as {}".format(address,username))
    displayName = username

def download_file(url, local_file_name):
    if not os.path.exists(local_file_name):
        r = requests.get(url, stream=True)
        with open(local_file_name, 'wb') as fd:
            for chunk in r.iter_content(1024): # parameter is chunk size in bytes
                fd.write(chunk)

download_file('https://pbaumgarten.com/uploads/python/bookface.png', "bookface.png")
root = Tk()
windowMainScreen = drawMainScreen(550, 400, "Bookface messenger")
root.withdraw() # Hide the root window, work with TopLevel windows instead
root.mainloop()
```
