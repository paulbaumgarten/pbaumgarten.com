# Google Custom Search

A far more reliable method of conducting Google Search is to sign up for an account with Google Cloud and use the Custom Google Search Engine API. Detailed and clear instructions can be found [https://stackoverflow.com/a/37084643](https://stackoverflow.com/a/37084643). It should be noted that only the first 100 queries per day are free, after that it is $5 per day per 1000 queries. You can, in the Google API management tools, impose a quote on your API key so you can't exceed the 100 per day limit. These instructions have been largely copied from the linked StackOverflow.

Part 1 - Google Cloud account and activate API

1. Sign up for a Google Cloud account at https://cloud.google.com (you will need a credit card for this)
2. Search the APIs to find the Custom Google Search.
3. Activate it. 
4. Generate an API key (and make a copy of it).
5. Adjust your quota to limit yourself to the 100 queries per day.

Part 2 - Custom Search engine

1. From the Google Custom Search homepage ( http://www.google.com/cse/ ), click Create a Custom Search Engine.
2. Type a name and description for your search engine.
3. Under Define your search engine, in the Sites to Search box, enter at least one valid URL (For now, just put www.anyurl.com to get past this screen. More on this later ).
4. Select the CSE edition you want and accept the Terms of Service, then click Next. Select the layout option you want, and then click Next.
5. Click any of the links under the Next steps section to navigate to your Control panel.
6. In the left-hand menu, under Control Panel, click Basics.
7. In the Search Preferences section, select Search the entire web but emphasize included sites.
8. Click Save Changes.
9. In the left-hand menu, under Control Panel, click Sites.
10. Delete the site you entered during the initial setup process.

Part 3 - Python library

```sh
pip3 install --user google-api-python-client
```

Part 4 - Python code

```python
from googleapiclient.discovery import build

api_key = "---insert-your-api-key-here---"
custom_search_engine_id = "---insert-your-custom-engine-id-here---"

def google_search( query, api_key, custom_search_engine_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=custom_search_engine_id, **kwargs).execute()
    return result["items"]

if __name__=="__main__":
    query = input("What would you like me to search for?")
    results = google_search(query, api_key, custom_search_engine_id, num=1)
    response = "The top result is from {} and it starts with {}".format(results[0]["displayLink"], results[0]["snippet"])
    print(response)
```

For example, a search for "Perth" outputed the following: *The top result is from en.wikipedia.org and it starts Perth is the capital and largest city of the Australian state of Western Australia. It is the fourth-most populous city in Australia, with a population of 2,022,044 living*.
