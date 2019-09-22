# Dates & times

## Creating a datetime

```python
from datetime import datetime

# Create a datetime using current computer date & time
now = datetime.now()

# Create a datetime from numeric day, month, year values
christmas = datetime( 2019, 12, 25 )

# Create a datetime from year=2019, month=12, day=25, hour=11, minute=00, seconds=00
christmas = datetime( 2019, 12, 25, 11, 00, 00 )

# Create a datetime from a formatted string
# - See section below about formatting the string
birth_text = input("What is your birthday (write it as dd/mm/yyyy) ?")
birth_date = datetime.strptime(birth_text, "%d/%m/%Y")

# Create a datetime from a timestamp
timestamp = 1563958625      # Number of seconds since 01/01/1970 00:00 UTC
july24_2019 = datetime.fromtimestamp(timestamp)
```

## Creating a timestamp

* A timestamp is based on number of seconds since computing epoch, deemed as 01/01/1970 00:00 UTC

```python
from datetime import datetime
now = datetime.now()

# Create timestamp from a datetime object
timestamp = now.timestamp()
```

## Differences between dates

```python
from datetime import datetime
from datetime import timedelta

birth_text = input("What is your birthday (write it as dd/mm/yyyy) ?")
birth_date = datetime.strptime(birth_text, "%d/%m/%Y")
now = datetime.now()

# Create a timedelta automatically by subtracting two dates
diff = now - birth_date
print(f"You are currently {diff.days} days old!")

# Create a new date by adding a timedelta to a date
tenthousand = birth_date + timedelta( days=10000 )
print(f"You will be 10'000 days old on { tenthousand.strftime("%d %B, %Y") }")
```

For timedelta you may provide any combination of the following options:

* days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0

## Create formatted strings

Use `strftime()` to generate strings containing dates and times in human presentable formats for your users

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

## Parts of dates

To retrieve parts of a date or time

```python
from datetime import datetime

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = datetime.now()

print(f"The year is { now.year }")
print(f"The month is { now.month }")
print(f"The day is { now.day }")
print(f"The hour is { now.hour }")
print(f"The minute is { now.minute }")
print(f"The second is { now.second }")
today_name = day_names[ now.weekday() ] # 0 = Monday
print(f"The day of week is { today_name }") 
```

## Replace parts of a date

Use the date `.replace()` function

```python
from datetime import datetime

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
birth_text = input("What is your birthday (write it as dd/mm/yyyy) ?")
birth_date = datetime.strptime(birth_text, "%d/%m/%Y")
now = datetime.now()

this_year = birth_date.replace( year = now.year )  # Replace the year

weekday_number = this_year.weekday()
print(f"Your birthday this year is a {day_names[ weekday_number ]")
```

## Problem set

1. Write a function that, given a string in date format, will calculate and return your age in years. Example `getAge("01/01/2010") returns 9`.
2. Write a function that, given a string in date format, will calculate and return your age in years with one decimal point. `getAgeDecimal("01/01/2010") returns 9.7`.
3. Write a function that, given a string in date format, will calculate and return your age in years, months, days. `getAgeLong("01/01/2010") returns 9, 10, 1`.
4. Write a function that, given a string in date format, will calculate and return the number of days until your next birtday. `getDaysUntilBirthday("01/01/2010") returns 71`.
5. Write a function that, given a string in date format, will calculate and return the day of week as a string for that date. `getDayOfWeek("01/01/2010") returns "Tuesday"`.
6. Write a function accepting two dates, return True if the first is the earlier date, False if it is the later date. Example function call being `firstDateIsFirst( "04/06/2018", "02/08/2016" )`
7. Given a list of dates as a function paramter (given as strings in DD/MM/YYYY format), and sort them into calendar correct order from earliest to latest and return the list. Example input being `sortdates( ["03/05/2001", "01/04/2002", "13/01/2000"] )`.

