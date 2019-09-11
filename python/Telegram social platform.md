# Telegram

Telegram is social media messaging platform like Whatsapp or iMessage. They have quite a "developer friendly" framework, so I recommend it as the starting point if you want to build a project that interacts with a messaging platform that you can use via your phone.

* [Visit the Telegram website](https://telegram.org/)

# Requirements

Requires the following Python packages:

* `python-telegram-bot==12.0.0b1`
* `pillow` (for the camera part of the demo)
* `opencv-contrib-python` (for the camera part of the demo)
* `numpy` (for the camera part of the demo)

If you use pip run `pip install python-telegram-bot pillow opencv-contrib-python numpy` (remember to use `sudo` or `pip3` if you usually have do)

Note: to install the version 12 beta, the pip command is

```bash
pip install python-telegram-bot==12.0.0b1 --upgrade
```

# Step 1 - Chat with the BotFather

* Install the Telegram app if you don't already have it
* When creating your account, you will need to allow the app to verify your phone number, but once that is done you can safely revoke that permission in your phone settings
* Not sure about iOS, but on Android it is safe to deny permission to import your contacts, access your photos etc (unless, of course, you want to send photos to your bot later)
* Following the screenshots below: Search for the `BotFather` account, send it a `/newbot` command, answer the questions and write down your API token.

![](img/telegram-botfather.jpg)

# Step 2 - Test with demo code

* Note: the `camera` module used in the following example is my example one provided [here](/python/camera)

```python
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from datetime import datetime
import logging
import telegram
import camera
from PIL import Image

api_key = "---insert-your-api-key---"
owner_id = 000000000 # Add your telegram ID number here

# Initiate logging
logging.basicConfig(filename="python.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Webcam
cam = camera.Camera()

def photo(update, context):
    print("photo request received")
    cam.save_photo("photo.jpg")
    update.message.reply_photo(photo=open('photo.jpg', 'rb'))

def hello(update, context):
    print("hello received ",update.message.chat_id)
    date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
    uid = update.message.from_user
    update.message.reply_text("Hello {}! Test was received at {}".format(uid.username, date_str))

def echo(update, context):
    print("echo received ",update.message.chat_id)
    date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
    uid = update.message.from_user 
    msg = update.message.text
    update.message.reply_text("Hello {}! You said: {}".format(uid.first_name, msg))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == "__main__":
    print("Welcome")
    cam.save_photo("photo.jpg")
    # Create the bot object
    updater = Updater(token=api_key, use_context=True)
    me = updater.bot.get_me()
    print("Welcome to my Telegram bot")
    print("username:     "+me['username'])
    print("display name: "+me['first_name'])
    # Setup response paths
    updater.dispatcher.add_handler(CommandHandler("hello", hello))
    updater.dispatcher.add_handler(CommandHandler("photo", photo))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling() # Start the bot (non-blocking)
    updater.bot.send_message(chat_id=owner_id, text="PhotoBot has started.")
    updater.idle() # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
```

# Step 3 - Make it your own

## Responding to commands

Telegram commands are messages that begin with a `/` such as `/whoami`.

To create a handler that responds to this command that will run the `who_am_i()` function, add a CommandHandler as follows:

```python
    updater.dispatcher.add_handler(CommandHandler('whoai', who_am_i))
```

The template for your response function would then look like

```python
def who_am_i(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /whoami command")
    # do something interesting
    update.message.reply_text("It's too early in the morning for such a deep question!")
```

It is possible to receive commands with various parameters. For instance, you could use `/getfile photo1.jpg` (please implement security checks on who you are replying to!). The parameters are in a python list at `context.args`. For instance:

```python
trusted_whitelist = [999999999]

def sendfile(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /sendfile command")
    if update.message.from_user.id in trusted_whitelist:
        for filename in context.args:
            print(sender+": Sending file "+filename)
            update.message.reply_document(text="Have a file...", document=open(filename, 'rb'))
```

## Responding to text messages

Messages that do not start with a `/` are simply text. You can process these as you like as well. Really there's no reason you couldn't run commands based off their content as well, it's just a Telegram convention that commands start with the slash so there is a built in handler to help deal with them.

The normal handler for a text message that would call a function called `echo()` would be:

```python
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
```

The template for your response function would then look like

```python
def echo(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent a message")
    # do something interesting
    update.message.reply_text("You said: "+update.message.text)
```

## Sending a text message

* In reply to an existing message

```python
    update.message.reply_text("Hello!")
```

* As a new message

```python
    updater.bot.send_message(chat_id=owner_id, text="PhotoBot has started.")
```

## Receiving a photo/video/audio/file

This helpful `got_file()` function will accept most file types and save them for you automatically into a downloads folder of your choosing.

```python
def got_file(update, context):
    global folder # eg, folder = "downloads/"
    file_id = None
    bot = None
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    if update.message.audio:
        print(sender+": Send an audio message")
        file_id = update.message.audio.file_id
        bot = update.message.audio.bot
    elif update.message.document:
        print(sender+": Sent a document")
        file_id = update.message.document.file_id
        bot = update.message.document.bot
    elif update.message.photo:
        print(sender+": Sent a photo")
        file_id = update.message.photo[-1].file_id
        bot = update.message.photo[-1].bot
    elif update.message.video:
        print(sender+": Sent a video")
        file_id = update.message.video.file_id
        bot = update.message.video.bot
    elif update.message.video_note:
        print(sender+": Sent a video note")
        file_id = update.message.video_note.file_id
        bot = update.message.video_note.bot
    elif update.message.voice:
        print(sender+": Sent a voice message")
        file_id = update.message.voice.file_id
        bot = update.message.voice.bot
    if file_id and bot:
        new_file = bot.get_file(file_id)
        extension = (new_file.file_path).split(".")[-1] # get file extension of received file
        datetime_str = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        file_name = folder + datetime_str + "-" + str(update.message.chat_id) + "." + extension
        new_file.download(file_name)
        print("Downloaded file: {}".format(file_name))
    else:
        print("Unable to download file")
```

* Handler(s) to add

```python
    # Response paths for various file attachment types, can all go to same handler
    updater.dispatcher.add_handler(MessageHandler(Filters.audio, got_file))
    updater.dispatcher.add_handler(MessageHandler(Filters.document, got_file))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, got_file))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, got_file))
    updater.dispatcher.add_handler(MessageHandler(Filters.video, got_file))
    updater.dispatcher.add_handler(MessageHandler(Filters.video_note, got_file))
```

## Sending a photo message

* In reply to an existing message

```python
folder = "downloads/"
photo_whitelist = [ 111111111, 222222222, 333333333 ] # Telegram userid of trusted accounts

def photo(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /photo")
    if update.message.from_user.id in photo_whitelist: # only those we trust
        print("Photo request allowed")
        cam.save_photo("photo.jpg")
        update.message.reply_photo(photo=open('photo.jpg', 'rb'))
    else:
        print("Photo request denied")
        update.message.reply_text("Denied")
```

The `photo=` parameter can be a file from disk, website address, of PIL image from memory. Refer to the examples in the "as a new message" section as they are the same format.

* As a new message

```python
# from your disk
updater.bot.send_photo(chat_id=chat_id, photo=open('tests/test.png', 'rb'))

# from a website or online source
updater.bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')

# from an image loaded into memory
img = Image() # PIL Image object
# or .... img = camera.Camera().get_photo() # to use the above linked camera module
updater.bot.send_photo(chat_id, photo=img)

# An animated gif
url = "https://www.website.com/animated.gif"
settings = {
    duration=None, 
    width=None, 
    height=None, 
    thumb=None, 
    caption=None, 
    parse_mode=None, 
    disable_notification=False, 
    reply_to_message_id=None, 
    reply_markup=None, 
    timeout=20
}
updater.bot.send_animation(chat_id, url, **settings)
```

## Sending a video message

* In reply to an existing message

```python
def send_video(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /sendvideo command")
    # do something exciting
    update.message.reply_audio(text="Have a video...", audio=open('recording.mp4', 'rb'))
```

* As a new message

```python
updater.bot.send_video(chat_id=chat_id, video=open('recording.mp4', 'rb'))
```

## Sending an audio message

* In reply to an existing message

```python
def send_audio(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /sendaudio command")
    # do something exciting
    update.message.reply_audio(text="Have a video...", audio=open('recording.mp3', 'rb'))
```

* As a new message

```python
updater.bot.send_audio(chat_id=chat_id, audio=open('recording.mp3', 'rb'))
```

Note: for OGG files, use `reply_voice` and `send_voice` as appropriate;

* `update.message.reply_voice(text="Have a document...", audio=open('recording.ogg', 'rb'))`
* `updater.bot.send_voice(chat_id=chat_id, voice=open('recording.ogg', 'rb'))`

## Sending a different type of file

* In reply to an existing message

```python
def sendfile(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /sendfile command")
    update.message.reply_document(text="Have a document...", document=open('tests/test.zip', 'rb'))
```

* As a new message

```python
    updater.bot.send_document(chat_id=chat_id, document=open('tests/test.zip', 'rb'))
```

## Sending buttons in a message / receiving response

* Import

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
```

* Send buttons as a message reply

```python
def paperrocksissors(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /play command")
    # send buttons as a reply
    buttons = [
        [ # start a row
            InlineKeyboardButton("Paper", callback_data="button1"),
            InlineKeyboardButton("Rock", callback_data="button2"),
        ],[ # start next row
            InlineKeyboardButton("Sissors", callback_data="button3")
        ] # end of row
    ] # end of buttons
    buttons_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("What will it be?", reply_markup=buttons_markup)
```

* Send buttons as a new message

```python
    buttons = [
        [ # start a row
            InlineKeyboardButton("Paper", callback_data="button1"),
            InlineKeyboardButton("Rock", callback_data="button2"),
        ],[ # start next row
            InlineKeyboardButton("Sissors", callback_data="button3")
        ] # end of row
    ] # end of buttons
    buttons_markup = InlineKeyboardMarkup(buttons)
    updater.bot.send_message(chat_id=owner_id, text="What will it be?", reply_markup=buttons_markup)
```

* Process response

```python
def button(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Clicked a button!")
    # this function is run when the button click is received
    clicked = update.callback_query.data # callback_query.data contains the text that was set in `callback_data`
    print("button was pressed! clicked = {}".format(clicked))
    update.callback_query.edit_message_text(text="Selected option: {}".format(clicked))
```

* Handler to add

To handle the callback_data, you need to set a CallbackQueryHandler specifying the callback function.

```python
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
```

## Sending a request for GPS / receiving GPS

* Request a contact as a reply

```python
def whereami(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /whereami command")
    location_keyboard = telegram.KeyboardButton(text="Send my GPS location", request_location=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[ location_keyboard ]])
    update.message.reply_text(text="Share location?", reply_markup=reply_markup)
```

* Request a contact as a new message

```python
    location_keyboard = telegram.KeyboardButton(text="Send my GPS", request_location=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[ location_keyboard ]])
    updater.bot.send_message(chat_id=owner_id, text="PhotoBot has started.", reply_markup=reply_markup)
```

* Processing the response

```python
def got_location(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent GPS location")
    gps = update.message.location
    print("Latitude: {}, Longitude: {}".format(gps.latitude, gps.longitude))
```

* Handler to add

```python
    updater.dispatcher.add_handler(MessageHandler(Filters.location, got_location))
```

## Sending a request for contact / receiving contact info

* Request a contact as a reply

```python
def whoami(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent /whoami command")
    contact_keyboard = telegram.KeyboardButton(text="Send my contact info", request_contact=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[ contact_keyboard ]])
    text = "Share your contact info?"
    update.message.reply_text(text, reply_markup=reply_markup)
```

* Request a contact as a new message

```python
    send_to_id = 00000000 # telegram id number
    contact_keyboard = telegram.KeyboardButton(text="Send my contact", request_contact=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[ contact_keyboard ]])
    updater.bot.send_message(chat_id=send_to_id, text="PhotoBot has started.", reply_markup=reply_markup)
```

* Processing the response

```python
def got_contact(update, context):
    sender = update.message.from_user.username + " ("+str(update.message.from_user.id)+")"
    print(sender+": Sent contact information")
    contact = update.message.contact
    print("Given name:   "+contact.first_name)
    print("Family name:  "+contact.last_name)
    print("Telegram ID:  "+str(contact.user_id))
    print("Phone number: "+contact.phone_number)
```

* Handler to add

```python
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, got_contact))
```

## Structure of some common objects

update.message.from_user

```python
{
    'id': 999999999, 
    'first_name': 'John', 
    'is_bot': False, 
    'last_name': 'Doe', 
    'username': 'johndoe', 
    'language_code': 'en'
}
```

update.message

```python
    {
        'message_id': 124, 
        'date': 1550868972, 
        'chat': {
            'id': 999999999, 
            'type': 'private', 
            'username': 'johndoe', 
            'first_name': 'John', 
            'last_name': 'Doe'
        }, 
        'text': 'What will it be?', 
        'entities': [], 
        'caption_entities': [], 
        'photo': [], 
        'new_chat_members': [], 
        'new_chat_photo': [], 
        'delete_chat_photo': False, 
        'group_chat_created': False, 
        'supergroup_chat_created': False, 
        'channel_chat_created': False, 
        'from': {
            'id': 999999999, 
            'first_name': 'demo', 
            'is_bot': True, 
            'username': 'demo_bot'
        }
    }
```

bot

```python
{
    'id': 999999999, 
    'username': 'demo', 
    'first_name': 'demo_bot'
}
```

video_note

```python
{
    'file_id': 'DQADBAADigUAAruhkFNv9oDDBD4AAZwC', 
    'length': 240, 
    'duration': 2, 
    'thumb': {
        'file_id': 'AAQEABPw-iobAASmnLpP_6jZ4vCIAAIC', 
        'width': 240, 'height': 240, 'file_size': 6180
    }, 
    'file_size': 68268
}
```

# References

https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#send-a-chat-action

