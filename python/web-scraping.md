# BeautfulSoup4 - Web scraping

The following example recipes were correct at the time of printing. Be aware, however, that they may break whenever the owner of the website changes the layout/structure/programming of their website.

Requires:           BeautifulSoup4  
Package to add:     bs4  
Documentation at:   https://www.crummy.com/software/BeautifulSoup/bs4/doc/  

## Initialise

```python
import requests
from bs4 import BeautifulSoup
# Execute a web request
params = {}
headers = {}
url = "https://www.wunderground.com/weather/ch/lausanne"
response = requests.get(url, params=params, headers=headers)
# Get the HTML string
html = response.content.decode(response.encoding)
# Load the BeautifulSoup parser
soup = BeautifulSoup(html, "html.parser")
```

## Searching a HTML tree

`soup.find()` will return the first match, whereas `soup.find_all()` will return a list of matches.

* if using `.find()` you should run a check on the results to see if *anything* was found first. eg: `result = soup.find('div')` followed by `if result:`.
* if using `.find_all()`, you can simply iterate through the resulting list, or check `len(result)`.

You can search for tags and/or attributes as the following examples illustrate:

```python
result = soup.find_all("div")
result = soup.find_all( attrs={"class":"heading"} )
result = soup.find_all( "h1", attrs={"class":"heading"} )
```

You can also run soup requests on soup results. eg:

```python
result = soup.find_all("div")
for item in result:
    sub_result = item.find_all("p")
```

## Getting info about the tag(s) found

If `result` is a single tag from a `find`, or an element of a list being iterated over from a `find_all()`, then:

* `result.name` ... the name of the tag, eg "h1"
* `result["href"]` ... the value of the attribute
* `result["class"]` ... note: because class can contain multiple values, this will return a list of strings!
* `result.string` ... the innerText of a tag

## Navigating to other tags

* `len(tag.contents)` ... will tell you the size of the resulting list
* `kids = tag.contents` ... Will only return DIRECT children (ie: not grand-children etc)
* `legacy = tag.descentants` ... Will return all children, grand-children, and so on recursively
* `adults = tag.parent` ... Will return the parent tag
* `brother = tag.next_sibling`
* `sister = tag.previous_sibling`

<div class="page"/>

## Recipe: Listen to a song on YouTube

```python
import json
import requests

def get_youtube_search(query):
    from bs4 import BeautifulSoup
    # Web request
    params = {
        "search_query": query
        }
    url = "https://www.youtube.com/results"
    response = requests.get(url, params=params)
    html = response.content.decode("utf-8")
    # Parse the result through BS
    soup = BeautifulSoup(html, "html.parser")
    vid = soup.find(attrs={'class': 'yt-uix-tile-link'})
    print("Found: ",vid.contents)
    return 'https://www.youtube.com' + vid['href']

def open_url_in_browser(url):
    import webbrowser
    webbrowser.open(url, new=2) # 2 = open in new tab

# Test it works
if __name__ == "__main__":
    search_for = input("What would you like to play in Youtube? ")
    vid = get_youtube_search( search_for )
    open_url_in_browser(vid + "&autoplay=1")
```

## Recipe: Google search

```python
def google_search(query):
    from bs4 import BeautifulSoup
    params = {
        "q": query,
        "hl": "en"
        }
    headers = {
        "accept-encoding": "gzip"
        }
    url = "https://www.google.com/search"
    response = requests.get(url, params=params, headers=headers)
    html = response.content.decode(response.encoding)
    # Process with beautifl soup
    soup = BeautifulSoup(html, "html.parser")
    info = soup.find(attrs={"class": "mraOPb"})
    if info:
        for item in info.children:
            return(item.get_text())

# Test it works
if __name__ == "__main__":
    search_for = input("What would you like to Google search for? ")
    result = google_search( search_for )
    print(result)
```

Note: A far more reliable method of conducting Google Search is to sign up for an account with Google Cloud and use the Custom Google Search Engine API. Detailed and clear instructions can be found [https://stackoverflow.com/a/37084643](https://stackoverflow.com/a/37084643). It should be noted that only the first 100 queries per day are free, after that it is $5 per day per 1000 queries. You can, in the Google API management tools, impose a quote on your API key so you can't exceed the 100 per day limit. See the heading below.

<div class="page"/>

## Recipe: Play a YouTube channel's most recent video

```python
import json
import requests

def get_youtube_channel_search(query):
    from bs4 import BeautifulSoup

    # Step 1 - Search for the channel
    params = {
        "search_query": query+" channel"
        }
    headers = {
        "accept-encoding": "gzip"
        }
    url = "https://www.youtube.com/results"
    response = requests.get(url, params=params, headers=headers)
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    channel = soup.find(attrs={'class': 'yt-uix-tile-link'})
    print("Found: ",channel.contents)

    # Step 2 - Look up the channel for the most recent video
    url = "https://www.youtube.com" + channel.get("href") + "/videos?flow=grid&view=0&sort=dd"
    response = requests.get(url, params=params)
    html = response.content.decode(response.encoding)
    soup = BeautifulSoup(html, "html.parser")
    vid = soup.find(attrs={'class': 'yt-uix-tile-link'})
    print("Found: ",vid.contents)
    return 'https://www.youtube.com' + vid['href']

def open_url_in_browser(url):
    import webbrowser
    webbrowser.open(url, new=2) # 2 = open in new tab

# Test it works
if __name__ == "__main__":
    search_for = input("What would you like to play in Youtube? ")
    vid = get_youtube_channel_search( search_for )
    open_url_in_browser(vid + "&autoplay=1")
```

<div class="page"/>


## Recipe: Google News

```python
import requests
from bs4 import BeautifulSoup

def saveFile( filename, content ):
    with open(filename, "w") as w:
        w.write(content+"\n")

if __name__ == "__main__":
    # Load the content of the website
    url = "https://news.google.com/gn/news/?hl=en"
    page = requests.get(url)
    print( page.content ) # Will print the content of the webpage

    # Run our page through BeautifulSoup and prettify it
    soup = BeautifulSoup( page.content, "html.parser" )
    pretty = soup.prettify()
    saveFile( "output.txt", pretty )

    # Let's get the news headlines
    print( "Page title: "+soup.title.string )

    for headline in soup.find_all("a", role="heading", limit=20):
        print( headline.string ) # the text content inside the tag
            print( headline.get("href") ) # get content of the href attribute
```

## Recipe: ABC News

```python
import requests
from bs4 import BeautifulSoup

def saveFile( filename, content ):
    with open(filename, "w") as w:
        w.write(content+"\n")

if __name__ == "__main__":
    # Load the content of the website
    url = "https://news.google.com/gn/news/?hl=en"
    page = requests.get(url)
    print( page.content ) # Will print the content of the webpage

    # Run our page through BeautifulSoup and prettify it
    soup = BeautifulSoup( page.content, "html.parser" )
    pretty = soup.prettify()
    saveFile( "output.txt", pretty )

    # Let's get the news headlines
    print( "Page title: "+soup.title.string )

    for headline in soup.find_all("a"):
        if headline.parent.parent.get("class") is not None:
            if "doctype-article" in headline.parent.parent.get("class"):
                print( headline.string ) # the text content inside the tag
                print( headline.get("href") ) # get content of the href attribute
```

## Function reference

The documentation needs work, but for what it is, you can find it here:

* https://www.crummy.com/software/BeautifulSoup/bs4/doc/

