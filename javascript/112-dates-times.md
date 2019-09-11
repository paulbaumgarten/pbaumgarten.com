# 1.12 - Dates and times

We've used code that used date and time functionality in a couple of exercises already. Working with dates and times is a fairly common task for a program and there are a bunch of useful Javascript commands we can use for this.

```javascript
let today = new Date();

console.log("The date is",today.toLocaleDateString());
console.log("The time is",today.toLocaleTimeString());

let epoch = today.getTime() / 1000;
console.log("The number of seconds since midnight 01/01/1970 is",epoch)
/*
Computer programs internally use this unit of time for a lot of purposes, you will see it come up again and again. It is useful for you to understand that the number of seconds since 01/01/1970 is significant as you will see it again and again. Curiously, in the case of Javascript, the getTime() function provides the epoch as milliseconds, hence the division by 1000. There is also a corresponding setTime() function you can use as shown below.
*/
```

When we create a new date variable (more technically the Date is known as an object, a distinction we'll worry about later), there are a few different ways we can instantiate it (create it).

* `let today = new Date();` - this is the most basic and you've already seen it several times. It will set the current date and time into the object called 'today'. Note: The time doesn't continue updating as the program continues running, it is what the time was at the moment that line of code executed.
* `let solstice = new Date( 1561118400000 );` - this creates a date/time object where the inputting value represents the number of milliseconds since midnight 1/1/1970 (see the note about the significance of that above).
* `let solstice = new Date( 2019, 5, 21 );` - this creates an object set to the 21st of June 2019. Two things to note: The order of the parameters is from largest chunk of time to smallest (year, month, day), and the month needs to always be one value lower than the number the human calendar associates with the month because this is one truly sucky thing about Javascript (ie: 0=January, 1=February, ... 11=December). So... yup.
*  `let my_birthday = new Date( 2019, 6, 29, 19, 20, 0 );` - this initialises a date and time value, again based on order of values being from largest chunk of time to smallest (year, month, day, hour, minute, second). Also, again, the month must be one value lower than intended.

So, let's practice creating datetime objects that aren't just the current date. For instance, do you know what day of the week your birthday was? Let's find out!

```javascript
let birthday_text = prompt("What is your birthday (write it as dd/mm/yyyy) ?")
let parts = birthday_text.split("/");
let birthday_date = new Date(parts[2], parts[1]-1, parts[0]);  // year, month-1, day, hours, minutes, seconds
let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
console.log("I understood that as",birthday_date.toLocaleDateString());
console.log("Which was, by the way, a", days[ birthday_date.getDay() ] );
```

## Differences between dates

```javascript
let birthday_text = prompt("What is your birthday (write it as dd/mm/yyyy) ?")
let parts = birthday_text.split("/");
let birthday_date = new Date(parts[2], parts[1]-1, parts[0]);  // year, month-1, day, hours, minutes, seconds
let today = new Date();
let milliseconds_per_day = 24 * 60 * 60 * 1000;
let difference = today - birthday_date;
let days_old = Math.trunc( difference / milliseconds_per_day );
console.log("You are ",days_old," days old!")

let five_thousand = new Date(birthday_date.getTime() + milliseconds_per_day*5000);
let ten_thousand = new Date(birthday_date.getTime() + milliseconds_per_day*10000);

if (five_thousand < today) {
   console.log("Did you know your 5'000th day was",five_thousand.toLocaleDateString());
} else {
   console.log("Did you know your 5'000th day will be",five_thousand.toLocaleDateString());
}
if (ten_thousand < today) {
   console.log("Did you know your 10'000th day was",ten_thousand.toLocaleDateString());
} else {
   console.log("Did you know your 10'000th day will be",ten_thousand.toLocaleDateString());
}
```

## Numeric values from dates and times

In addition to working with converting dates to strings, we can also extract the numeric values for each component of a date or time.

```javascript
let birthday_text = prompt("What is your birthday (dd/mm/yyyy)?");
let parts = birthday_text.split("/");
let dob = new Date(parts[2], parts[1]-1, parts[0]);
let today = new Date();
let this_year_bday = new Date(today.getFullYear( ), dob.getMonth(), dob.getDay());
let age_this_year = today.getFullYear() - dob.getFullYear();
let diff = (today - this_year_bday) / (24*60*60*1000);
if (diff > 0) {
    console.log("Your most recent birthday was ",diff," days ago. You turned ",age_this_year);
} else if (diff < 0) {
    console.log("Your next birthday is ",diff," days ago. You will turn ",age_this_year);
} else {
    console.log("It's your birthday! Happy birthday! You are ",age_this_year);
}
```

For the record, the following are the key functions for the date object you should have in your repertoire, assuming a date object called `today`:

Setting date/time values

* `today.setFullYear( 2018 );`
* `today.setMonth( 0 );` - remember to subtract 1, so 0 = January
* `today.setDate( 1 );`
* `today.setHours( 23 );` - 24 hour clock
* `today.setMinutes( 59 );`
* `today.setSeconds( 59 );`
* `today.setTime( 1561118400000 );` - milliseconds since 1/1/1970

Getting date/time values

* `let y = today.getFullYear();`
* `let m = today.getMonth() + 1;` - remember to add 1
* `let d = today.getDate();`
* `let dayOfWeek = today.getDay();`
* `let h = today.getHours();`
* `let m = today.getMinutes();`
* `let s = today.getSeconds();`
* `let t = today.getTime();` - milliseconds since 1/1/1970
* `let tz = today.getTimezoneOffset();` - local timezone difference from UTC in number of minutes

Getting date/time strings

* `today.toDateString()` - returns a string in the form of "Wed Jul 28 1993"
* `today.toISOString()` - returns a string using offical ISO format eg "2011-10-05T14:48:00.000Z"
* `today.toLocaleDateString()` - returns a date where the layout will vary depending on the local system (eg: mm/dd/yyyy for US, dd/mm/yyyy for UK)
* `today.toLocaleTimeString()` - returns a time where the layout will vary depending on the local system

---