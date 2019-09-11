# YouTube downloading

Install packages

```bash
sudo pip install youtube_dl pafy requests --upgrade
```

Basic recipe to search Youtube with a query

```python
from bs4 import BeautifulSoup
import requests

def search(query):
    params = {"search_query": query}
    url = "http://www.youtube.com/results"
    response = requests.get(url, params=params)
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    vids = soup.find_all(attrs={'class': 'yt-uix-tile-link'})
    results = []
    for vid in vids:
        href = vid["href"]
        if href[0:9] == "/watch?v=":
            href = vid["href"]
            videoid = href[9:]
            if "&" in href:
                href = href[ : href.index("&") ]
            url = "https://www.youtube.com" + href
            title = vid["title"]
            results.append( { "url": url, "title": title, "href": href, "id": videoid } )
    return results

q = input("Search Youtube: ")
results = search(q)
for item in results:
    print(f"Found video: {item['title']}")
    print(f"     at url: {item['url']}")
```

Basic recipe to download a video from YouTube

```python
import re
import pafy # https://github.com/mps-youtube/pafy

def download_youtube_video(url, folder=None):
    def _clean_file_name( original ):
        # Strip non-filename-friendly characters from the filename
        regex = re.compile('[^a-zA-Z0-9 \-.]')
        return regex.sub("", original )
    video = pafy.new(url, ydl_opts={'nocheckcertificate': True, "--no-check-certificate": True})
    best = video.getbestvideo(preftype="mp4")
    saveAs = _clean_file_name(video.title+"."+best.extension)
    if not folder==None:
        saveAs = os.path.join(folder, saveAs)
    best.download(quiet=True, filepath=saveAs)
    return saveAs

url = input("Enter youtube address of video to download")
download_youtube_video(url)

```

Basic recipe to download an audio track from YouTube

```python
import re
import pafy # https://github.com/mps-youtube/pafy

def download_youtube_audio(url, folder=None):
    def _clean_file_name( original ):
        # Strip non-filename-friendly characters from the filename
        regex = re.compile('[^a-zA-Z0-9 \-.]')
        return regex.sub("", original )
    video = pafy.new(url, ydl_opts={'nocheckcertificate': True, "--no-check-certificate": True})
    best = video.getbestaudio(preftype="m4a")
    saveAs = _clean_file_name(video.title+"."+best.extension)
    if not folder==None:
        saveAs = os.path.join(folder, saveAs)
    best.download(quiet=True, filepath=saveAs)
    return saveAs

url = input("Enter youtube address of audio to download")
download_youtube_audio(url)
```

