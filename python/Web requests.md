# Request - Getting data from the web

An API is an Application Programming interface. It is basically a gateway through which one program can access the data and services that a host organization is making available. It can be used for all sorts of things from weather, phone directories, google searches, contacts, facebook posts, twitter feeds etc etc.

There is no point giving you an comprehensive guide as every organization designs their API's differently. Most work on requiring you to sign up to obtain an API Key, a code that you send with your request to authorise access to their data. This is done by hosts to help guard against their systems being overloaded. If you have the option, choose to access data in JSON format. That is what this example is based on, and it is the most common these days. If you can't find an API for what you are looking for, you may want to consider using a web scraper such as Beautiful Soup (see related article).

* Comprehensive list of APIs available to the public: [https://github.com/toddmotto/public-apis](https://github.com/toddmotto/public-apis)

## Overview

The requests module is not provided by default, you will have to install it if you don't already have it

```bash
pip3 install requests
```

To use the requests module in your program, import it with

```python
import requests
```

The reqquests module supports HTTP GET, POST, PUT and DELETE requests as follows

```python
response = requests.get("http://www.example.com/")
response = requests.post("http://www.example.com/")
response = requests.put("http://www.example.com/")
response = requests.delete("http://www.example.com/")
```

### Attaching and uploading

* To attach parameters to your request, build a dictionary with your parameters to send and attach it to your request with the `params=` keyword argument

```python
p = { "v": "dQw4w9WgXcQ" }
response = requests.get("https://youtube.com/watch", params=p)
```

* To attach headers to your request (such a content-type), build a dictionary and attach it with the `headers=` keyword agument.
* To attach form-encoded data (mimicking an HTML form), pass a dictionary to the `data=` keyword argument.
* To attach cookies, send a dictionary to the `cookies=` keyword argument
* To attach a file upload to your request, attach a dictionary and pass it with the `files=` keyword argument as per example below.

```python
# Simple file upload
f = { 'file': open('report.pdf', 'rb') }
r = requests.post("https://httpbin.org/post", files=f)

# ... or to manually specify a filename and content_type
f = { 'file': ("newfilename.pdf", open('report.pdf', 'rb'), "application/pdf", {"Expires": "0"} ) }
r = requests.post("https://httpbin.org/post", files=f)

# ... or to upload a string as a file
f = { 'file': ("newfilename.pdf", data_string, "application/pdf", {"Expires": "0"} ) }
r = requests.post("https://httpbin.org/post", files=f)

```

### Responses

Some response attributes of interest

```python
status = response.status_code # 200 = ok
enc = response.encoding # for example `ISO-8859-1` or `UTF-8`
headers = response.headers # eg: content-type
cookies = response.cookies
```

For text responses:

```python
txt = response.text
```

For json responses:

```python
data = response.json()
```

For binary rexponses: Use `response.content`. 

* For example to download an image file, and open it directly into PIL

```python
from PIL import Image
from io import BytesIO
# ...
img = Image.open(BytesIO(response.content))
```

* For example to download and save a small file to disk

```python
with open('/tmp/metadata.pdf', 'wb') as f:
    f.write(response.content)
```

* For example to download a large file to disk

```python
url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
r = requests.get(url, stream=True) # note the stream=True
chunk_size = 2048 # number of bytes to download at a time

with open('/tmp/metadata.pdf', 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
```

## Examples

### Example: Random joke teller

```python
#!/usr/bin/env python3.7
import requests
import json
from datetime import datetime

def get_joke():
    url     = "https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke"
    params  = { }
    headers = { 'Content-Type': 'application/json' }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

answer = input("Do you want to hear a joke? (y/n) ")
while answer == "y":
    joke = get_joke()
    print( joke["setup"] )
    input()
    print( joke["punchline"] )
    print("")
    answer = input("Do you want to hear a joke? (y/n) ")
```

---

### Example: City latitude & longitude finder

```python
#!/usr/bin/env python3.7
import requests
import json
from datetime import datetime

def get_city_coordinates( location ):
    url     = "https://geocode.xyz/"+location+"?json=1"
    params  = { }
    headers = { 'Content-Type': 'application/json' }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

city = input("Type the name of a city: ")
info = get_city_coordinates(city)
print("City:      ",info["standard"]["city"])
print("Country:   ",info["standard"]["countryname"])
print("Latitude:  ",info["latt"])
print("Longitude: ",info["longt"])
```

---

### Example: Using the Swiss public transport API

Look up the Swiss public transport timetable for the next 10 departures from the stop at Clochatte.

* Documentation: https://timetable.search.ch/api/help

```python
import requests
import json
from datetime import datetime

# API settings
api_key = ""

# Function to perform the API request
def get_station_info(station_name, limit=10):
    url = "https://timetable.search.ch/api/stationboard.json"
    params = {
        "stop": station_name,
        "limit":"10"
        }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '{0}'.format(api_key)
        }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = json.loads(response.content.decode("utf-8"))
        # Print the forthcoming connections
        connections = data['connections']
        if isinstance(connections, list):
            messages = []
            for c in connections:
                departure_time = datetime.strptime(c["time"], "%Y-%m-%d %H:%M:%S")
                time_remaining = departure_time - datetime.now()
                minutes = int(time_remaining.total_seconds() / 60)
                destination = c["terminal"]["name"]
                messages.append("{0} {1} departs in {2} minutes bound for {3}".format(
                    c["type"], c["line"], minutes, destination))
            return(messages)
        else:
            return("Something has gone wrong :-(")
    else:
        return None

# Get the data
station_name = "Lausanne, Clochatte"
data = get_station_info(station_name)

# Print station name
print("Next departures for {0}".format(station_name))
for item in data:
    print(item)
```

---

### Example: Next SpaceX launch

```python
#!/usr/bin/env python3.7
import requests
import json
from datetime import datetime

def get_next_spacex():
    url     = "https://api.spacexdata.com/v2/launches/next"
    params  = { }
    headers = { 'Content-Type': 'application/json' }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

next_launch = get_next_spacex()
if next_launch != None:
    # Convert timestamp to human readable date
    launch_timestamp = next_launch["launch_date_unix"]
    launch_dt = datetime.fromtimestamp(launch_timestamp)
    launch_date_string = launch_dt.strftime("%d/%m/%Y %H:%M:%S")
    # Print info
    print("Next flight: ",next_launch["mission_name"])
    print("Date/time:   ",launch_date_string,"(your timezone)")
    print("Rocket:      ",next_launch["rocket"]["rocket_name"])
    print("Launch site: ",next_launch["launch_site"]["site_name_long"])
```

---

### Example: Weather for a given city

```python
#!/usr/bin/env python3.7
import json
import requests
import datetime
import os

# You will have to sign up for a free API KEY for this one to work
# Go to https://openweathermap.org/

def get_weather(api_key, location):
    url     = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(location, api_key)
    params  = { }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '{0}'.format(api_key)
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

WEATHER_API_KEY = "----insert-your-api-key-here----"
city = input("What city do you want the weather for?")
data = get_weather(WEATHER_API_KEY, city)
description = data["weather"][0]["description"]
kelvin = data["main"]["temp"]
celsius = round(kelvin-273.15)
message = "The weather in "+location+" is "+description+" and the temperature is "+str(celsius)
print(message)
```

---

### Example: Random cat or dog pics!

```python
#!/usr/bin/env python3.7
import requests
import json
from datetime import datetime
import urllib.request
from PIL import Image       # pillow

def get_cat_url():
    url     = "https://aws.random.cat/meow"
    params  = { }
    headers = { "Content-Type": 'application/json' }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

def get_dog_url():
    url     = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false"
    params  = { }
    headers = { "Content-Type": 'application/json' }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ",response.status_code," ***")
        return None

def download_file(url, file_name):
    urllib.request.urlretrieve(url, file_name)

def show_image(file_name):
    img = Image.open(file_name)
    img.show()

pic_info = get_dog_url()
print(pic_info[0])
download_file(pic_info[0], "random.jpg")
show_image("random.jpg")
```