# 1.15 - JSON

JSON (Java-Script Object Notation), is a commonly used format to exchange data on the internet. It includes the Javascript arrays we've already seen, but it also includes a method to store what's known as "key-value" pairs.

Examples:

Create an empty dictionary (see adding below to add items to an empty dictionary)

```javascript
let person = { };
```

Creating a json object with initial data

```javascript
let person = {"givenName" : "Paul", "familyName" : "Baumgarten"};
```

Getting elements from the json object

```javascript
// Method 1
console.log( person["givenName"] );
console.log( person["familyName"] );
// Method 2
console.log( person.givenName );
console.log( person.familyName );
```

* Note regarding the above: Method 2 looks nicer so, when would you bother with method 1? Primarily if you are using a variable to provide the name of the field you want to manipulate in the JSON. For instance, if you had `let field = "givenName";` you could then use `person[field]` to access `person["givenName"]`. You would not be able to do `person.field`, that won't work as it will try to find a field called field.

Adding / modifying elements in the json object

```javascript
person["email"] = "pbaumgarten@isl.ch";
person["website"] = "https://pbaumgarten.com";
```

Remove an element from the dictionary

```javacsript
delete person["website"];
```

Loop through all the elements of the dictionary

```javascript
for (let key in person) {
    if (person.hasOwnProperty(key)) {
        console.log("field "+key+" has value "+person[key]);
    }
}
```

---

## Bigger example

We can bring it all together with arrays as well.  For instance

```javascript
let people = [
    { "name": "Harry Potter", "house": "Gryffindor" },
    { "name": "Draco Malfoy", "house": "Slytherin" },
    { "name": "Newt Scamander", "house": "Hufflepuff" },
    { "name": "Ron Weasley", "house": "Gryffindor" },
    { "name": "Nymphadora Tonks", "house": "Hufflepuff" },
    { "name": "Luna Lovegood", "house": "Ravenclaw" },
    { "name": "Cedric Diggory", "house": "Hufflepuff" },
    { "name": "Filius Flitwick", "house": "Ravenclaw" },
    { "name": "Gilderoy Lockhard", "house": "Ravenclaw" },
    { "name": "Hermione Grander", "house": "Gryffindor" },
    { "name": "Severus Snape", "house": "Slytherin" },
    { "name": "Lord Voldemort", "house": "Slytherin" },
];

// Print a list of members
for (let person of people) {
    console.log("Did you know that "+person.name+" is in house "+person.house+"?");
}

/*
 Sort the array into house order

 (don't worry too much about the syntax of this, except to note that to use it with your own array of json objects, just replace the "a.house" and "b.house" with whichever field it is you are wanting to sort by)
*/
people.sort( function(a,b) { if (a.house < b.house) { return -1; } else { return 1; } } );

// Print a list of members again... notice the sort?
for (let person of people) {
    console.log("Did you know that "+person.name+" is in house "+person.house+"?");
}

// We could also just print the house name once, followed by a list of members
let currentHouse = "";
for (let person of people) {
    if (person.house != currentHouse) {
        console.log("Members of "+person.house+" are:");
        currentHouse = person.house;
    }
    console.log(" * "+person.name);
}

```

## Serialising & deserialising JSON

Serialising and deserialising are just fancy names for converting the data to a string, and then back again. The main reason we might want to do this is if we are exchanging data over the internet where strings are better "understood".

Here are some functions that are useful for getting started with JSON:

To convert a json object & array structure to a string:

```javascript
let str = JSON.stringify( obj );
```

To convert a string representation of objects & arrays back into a json object:

```javascript
let obj = JSON.parse( str );
```

---
