# Dictionaries

* Suggested video [Python Dictionaries](https://www.youtube.com/watch?v=XCcpzWs-CI4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=15)  by Socratica

Python dictionaries are similar to lists. Where a list uses a number to keep track of the individual elements contained within it, a dictionary (generally) uses a word.

Examples:

Create an empty dictionary (see adding below to add items to an empty dictionary)

```python
person = { }
```

Creating a dictionary with initial data

```python
person = {"givenName" : "Paul", "familyName" : "Baumgarten"}
```

Getting elements from the dictionary

```python
print( person["givenName"] )
print( person["familyName"] )
```

Adding / modifying elements in the dictionary

```python
person["email"] = "pbaumgarten@isl.ch"
person["website"] = "https://pbaumgarten.com"
```

Remove an element from the dictionary

```python
del person["website"]
```

Loop through all the elements of the dictionary

```python
for key,val in person.items():
  print("field "+key+" has value "+val)
```

## Read/write JSON files

A JSON file is a convienent file format for storing dictionary data. It is derived from the world of Javascript.

The following are two example functions that can be used for reading and writing JSON files.

```python
import json

def read_json( filename ):
    with open(filename, "r", encoding="utf-8") as f:
        content = json.load(f)
    return content

def write_json( filename, data ):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(f, data)
```

I have placed some common JSON data sets on Github you can test this with, [https://github.com/paulbaumgarten/data-sets](https://github.com/paulbaumgarten/data-sets).

The following example uses the `countries.json` data set.

```python
import files

countries = read_json("countries.json")
for val in countries:
    country = val["name"]
    code = val["code"]
    continent = val["continent"]
    print(f"The country {country} has code {code} and is in the continent of {continent}.")
```

## Requests

JSON is frequently used as the medium of transferring data between web servers and applications, as such knowledge of Python dictionaries can come in particularly useful for retrieving data from the internet. Take a look at my [Web requests](https://pbaumgarten.com/python/requests.html) notes for more detail.


# Problem sets

> You better believe these are coming soon! :-)
