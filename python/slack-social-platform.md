# Social message platforms

Integrating your project with one of the social message platforms can be a lot of fun. The easiest to integrate with is definately Telegram and is the one I would recommend for any first timers.

## Telegram

My Telegram instructions are quite extensive, so I've moved it to its own page.

* Go to my [Telegram](/python/telegram) page

## Slack

The following demo code works to send text and photo messages to a Slack account.

* Sign up to Slack
* To get your "oauth token", login to Slack, go to https://api.slack.com/apps , 
* Create an "app". Click on your app name, add features & functionality, permissions, oauth access token

```python
#!/usr/bin/env python3.7
import requests
import json
from datetime import datetime

slack_url = "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXX" # replace with your custom url
slack_oauth_token = "xoxp-000000000000-000000000000-0000000000000-00000000000000000000000000000000" # replace with your token
slack_channel = "XXXXXXXXX" # replace with your channel ID

def slack_send_message( url, message ):
    body  = { "text": message }
    headers = { 'Content-Type': 'application/json' }
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.content.decode(response.encoding)
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

def slack_upload_file( channel_id, filename ):
    url = "https://slack.com/api/files.upload"
    files = { 'file': open(filename, 'rb') }
    params = { "channels": [channel_id], "token": slack_oauth_token }
    response = requests.post(url, params=params, files=files)
    if response.status_code == 200:
        return response.content.decode(response.encoding)
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

f = "/users/pbaumgarten/ISL/isl/2019-11-design/lessons/10/cat.jpg"
response = slack_upload_file( slack_channel, f )
print("Response: ",response)

msg = input("Message to post to slack: ")
response = slack_send_message(slack_url, msg)
print("Response: ",response)
```

## Twitter

* [Twitter API instructions](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
* [Tweepy library](https://tweepy.readthedocs.io/en/3.7.0/index.html)
* [Suggested 1st tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library)

## Others

Another product that made it onto my shortlist but costs (an admittedly trivial) $5 after 7 days trial was [pushover.net](https://pushover.net/)

For most of the other platforms (Facebook, Instagram, Whatsapp), the barrier to integration is more complex, hence why I haven't written guides for those at this time. For beginner programmers, I would advise sticking to the ones already discussed if possible.

