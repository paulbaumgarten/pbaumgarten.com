# Dates and times

We've used code that used date and time functionality in a couple of exercises already. Working with dates and times is a fairly common task for a program and there are a bunch of useful Python commands we can use for this.

Python uses an object called `datetime` as the basis of it's date and time functionality. To load it into your program, you need to have an `import` command before you use it.

To import `datetime`, insert `from datetime import datetime` as the first line of your program, as the following simple example demonstrates.

## Creating datetime object

```python
# for current date & time
dt = datetime.now()
dt = datetime.utcnow()
print("The date and time is",dt)

# from given date & time
dt = datetime(2008, 11, 10, 17, 53, 59) # 2008-11-10 17:53:59
print("The date and time is",dt)

# from given string containing date & time
date_str = "2008-11-10 17:53:59"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("The date and time is",dt)

# from given timestamp (seconds since 1970-01-01 00:00 UTC)
timestamp = 1226527167
dt = datetime.fromtimestamp(timestamp)
dt = datetime.utcfromtimestamp(timestamp)
print("The date and time is",dt)
```

For example, do you know what day of the week your birthday was?

```python
from datetime import datetime

birthday = input("What is your birthday (write it as dd/mm/yyyy) ?")
dob = datetime.strptime(birthday, "%d/%m/%Y")
print("I understood that as",dob.strftime("%d %B, %Y"))
print("Which was, by the way, a",dob.strftime("%A"))
```

## Differences between dates

```python
from datetime import datetime
from datetime import timedelta

birthday = input("What is your birthday (write it as dd/mm/yyyy) ?")
dob = datetime.strptime(birthday, "%d/%m/%Y")
now = datetime.now()

diff = now - dob
print("You are ",diff.days," days old!")

fivethousand = dob + timedelta(days=5000)
tenthousand = dob + timedelta(days=10000)
if fivethousand < now:
   print("Did you know your 5'000th day was",fivethousand.strftime("%d %B, %Y"))
else:
   print("Did you know your 5'000th day will be",fivethousand.strftime("%d %B, %Y"))
if tenthousand < now:
   print("Did you know your 10'000th day was",tenthousand.strftime("%d %B, %Y"))
else:
   print("Did you know your 10'000th day will be",tenthousand.strftime("%d %B, %Y"))
```

## Numeric values from dates and times

In addition to working with converting dates to strings, we can also extract the numeric values for each component of a date or time.

```python
from datetime import datetime
from datetime import timedelta

birthday = input("What is your birthday (write it as dd/mm/yyyy) ?")
dob = datetime.strptime(birthday, "%d/%m/%Y")
now = datetime.now()

thisYearsBirthday = datetime( now.year, dob.month, dob.day )
diff = now - thisYearsBirthday

ageThisYear = now.year - dob.year

if diff.days > 0:
   print("Your most recent birthday was ",diff.days," ago. You turned ",ageThisYear)
elif diff.days < 0:
   print("Your next birthday is in ",abs(diff.days)," days. You turn ",ageThisYear)
else:
   print("It's your birthday! You are now ",ageThisYear,"!")
```

For the record, the following are the names of the various attributes that you can get numeric values for:

* dt.year
* dt.month
* dt.day
* dt.hour
* dt.minute
* dt.second
* dt.microsecond
* dt.tzinfo
* dt.tzname()
* dt.weekday() # 0 = Monday, 6 = Sunday 

## Datetime string format

You'll have noticed that both the `strptime()` (create a date/time from a string) and the `strftime()` (create a string from a date/time) commands use strings with weird looking percentage signs all over it. Those are special codes the commands use to know how to create/interpret the date. The meanings of each of those codes is as follows:

Day of week

* %a - Weekday abbreviated (eg: Sun)
* %A - Weekday full name (eg: Sunday)
* %w - Weekday number (0=Sunday 6=Saturday)

Day of month

* %d - Day of month (zero padded eg: 02)

Months

* %b - Month name abbreviated (eg: Jan)
* %B - Month full name (eg: January)
* %m - Month number (zero padded eg: 01)

Years

* %y - Year without century (zero padded)
* %Y - Year with century (zero padded)

Hours

* %H - Hour 24 hour clock (zero padded)
* %I - Hour 12 hour clock (zero padded)
* %p - AM or PM

Minutes

* %M - Minute (zero padded)

Seconds

* %S - Second (zero padded)

Timezones

* %z - Timezont UTC offset (eg: +0100)
* %Z - Timezone name

---

## Final datetime functionality

Just including a few other functions here for the sake of completeness. Timestamps (number of seconds since midnight 01/01/1970) are a useful method of calculating time lapsed.

```python
# Create a datetime from given timestamp (seconds since 1970-01-01 00:00 UTC)
timestamp = 1226527167
dt = datetime.fromtimestamp(timestamp)
dt = datetime.utcfromtimestamp(timestamp)

# current date & time to timestamp without having to create a datetime object
timestamp = datetime.now().timestamp()
timestamp = datetime.utcnow().timestamp()
```

## More information

* https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
* https://docs.python.org/3/library/datetime.html

---

