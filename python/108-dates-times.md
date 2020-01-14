# Dates & times

## Creating a datetime

Python uses the `DateTime` object to provide a programmer-friendly interface for managing all the different aspects of dates and times. This includes keeping track of leap years, the number of days in each month, timezones, day light saving where applicable and many other complications that start to appear where ever dates and times are involved.

```python
from datetime import datetime

# Create a datetime using current computer date & time
now = datetime.now()

# Create a datetime with year=2019, month=12, day=25
christmas = datetime( 2019, 12, 25 )
print(christmas)

# Create a datetime with year=2019, month=12, day=25, hour=11, minute=00, seconds=00
christmas = datetime( 2019, 12, 25, 11, 00, 00 )
print(christmas)

# Create a datetime from a formatted string
# - See section below about formatting the string
birth_text = input("What is your birthday (write it as dd/mm/yyyy) ?")
birth_date = datetime.strptime(birth_text, "%d/%m/%Y")
print(birth_date)
```

## Using timestamps

A timestamp is how computers internally store date and time information. Historically this is internally stored as the number of seconds since the computing epoch, deemed as 01/01/1970 00:00 UTC.

```python
from datetime import datetime

# Create a timestamp based on current date/time
timestamp = datetime.now().timestamp()

# Create a datetime from a timestamp
timestamp = 1563958625      # Number of seconds since 01/01/1970 00:00 UTC
july24_2019 = datetime.fromtimestamp(timestamp)
print(july24_2019)
```

## Differences between dates

We use the `timedelta` object to perform additions or subtractions with dates and times.

* `timedelta` accept sany combination of the following options: days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0

```python
from datetime import datetime, timedelta

apollo_11 = datetime( 1969, 7, 20, 20, 17, 40 )
now = datetime.now()

# Create a timedelta automatically by subtracting two dates
diff = now - apollo_11
print(f"Apollo 11 landed {diff.days} days ago!")

# Create a new date by adding a timedelta to a date
ten_thousand = now + timedelta( days=10000 )
print(f"10'000 days from today is { tenthousand.strftime("%d %B, %Y") }")
```

## Create formatted strings

While the `datetime` object is useful from a programming perspective, it will usually need converting to/from strings when being presented to the user, or receiving from the user.

Use `strftime()` to generate strings containing dates and times in human presentable formats for your users.

```python
# Create a date
apollo11 = datetime( 1969, 7, 20, 20, 17, 40 )

# Make pretty, human readable versions
pretty_date = apollo11.strftime("%A, %d %B, %Y")
pretty_time = apollo11.strftime("%H:%M:%S")

# Do something with them
print(f"Apollo 11 landed on the moon on {pretty_date} at the time of {pretty_time}")
```

Date based codes

* %a - Weekday abbreviated (eg: Sun)
* %A - Weekday full name (eg: Sunday)
* %d - Day number in month (zero padded eg: 02)
* %b - Month name abbreviated (eg: Jan)
* %B - Month full name (eg: January)
* %m - Month number (zero padded eg: 01)
* %y - Year without century (zero padded)
* %Y - Year with century (zero padded)

Time based codes

* %I - Hour 12 hour clock (zero padded)
* %H - Hour 24 hour clock (zero padded)
* %M - Minute (zero padded)
* %S - Second (zero padded)
* %p - AM or PM


## Get parts of dates/times

To retrieve parts of a date or time

```python
from datetime import datetime

apollo_11 = datetime( 1969, 7, 20, 20, 17, 40 )
y = apollo_11.year        # 1969
m = apollo_11.month       # 7 (July)
d = apollo_11.day         # 20
hr = apollo_11.hour       # 20 (8:00pm in 24 hr time)
mi = apollo_11.minute     # 17
se = apollo_11.second     # 40
wkd = apollo_11.weekday() # 6 (0=Monday so 6 is Sunday)
```

## Replace parts of a date

Use the date `.replace()` function

Example 1

```python
from datetime import datetime
date_1 = datetime(1980, 6, 20)
date_2 = date_1.replace( year = 2019 )  # Replace the year
print(date_2)   # 20/06/2019
```

Example 2

```python
from datetime import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
typed = input("What is your birthday (write it as dd/mm/yyyy) ?")
birthday = datetime.strptime(typed, "%d/%m/%Y")
now = datetime.now()
y = birthday.replace( year = now.year )  # Replace the year
day_number = y.weekday()
print(f"Your birthday this year is a {days[ day_number ]")
```

## Problem set

1. Write a function that, given a string in date format, will calculate and return your age in years. Example `getAge("01/01/2010") returns 9`.
2. Write a function that, given a string in date format, will calculate and return the number of days until the date. `get_days_until("01/01/2021") returns 312`.
3. Write a function that, given a string in date format, will calculate and return the day of week as a string for that date. `get_day_of_week("01/01/2010") returns "Tuesday"`.
4. Write a function accepting two dates that will return the number of days between the two dates. Example function call being `get_days_between( "04/06/2018", "02/08/2016" )`


