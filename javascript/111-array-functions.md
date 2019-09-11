# 1.11 - Other list/array functionality

## Splitting a string into an array of strings

We split strings the hard way before because we hadn't learnt about lists, but now we can use the easy method known as the `split()` function.

```javascript
let birthday = prompt("Please enter your date of birth as dd/mm/yyyy : ");
let parts = birthday.split("/");
console.log("Your day of birth is ", parts[0]);
console.log("Your month of birth is ", parts[1]);
console.log("Your year of birth is ", parts[2]);
```

## Joining a list together

Just as we can split a string into a list, we can join it back together again too.

```javascript
let addressList = ["Chemin de la Grangette 2","1052 Le Mont-sur-Lausanne","Switzerland"];
let newAddress = addressList.join(", ");
console.log(newAddress);
```

## Appending an item to a list

```javascript
let beatlesMembers = ["John", "Paul", "George"]
let beatlesMembers.push("Ringo")
```

## Deleting items from a list based on it's value

```javascript
let beatlesMembers = ["John", "Paul", "George", "Ringo"];
console.log(beatlesMembers);

let deleteThis = "Ringo";
let position = beatlesMembers.indexOf( deleteThis );
while (position >= 0) {
    beatlesMembers.splice(position, 1);
    position = beatlesMembers.indexOf( deleteThis );
}

console.log(beatlesMembers);
```

## Delete an item using it's index number.

```javascript
let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
days.splice(4 ,2);    // will remove 2 items from after the 4th value
console.log(days);    // let's have a 3 day week by deleting Thursdays and Fridays!
```

---
