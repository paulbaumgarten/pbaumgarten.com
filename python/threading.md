# Threads

Here is an example that uses threads to run a function, `clock_tick()` once a second. Note each instance of the `threading.Timer()` only calls `clock_tick()` once, hence why the function re-calls the Timer() each time it is run.

```python
import threading, time
from datetime import datetime
from datetime import timedelta

alarms = [ "8:25:00", "8:45:00", "9:30:00", "10:05:00", "10:50:00", "11:15:00", "11:55:00", "12:35:00", "13:35:00", "14:20:00", "14:55:00", "15:40:00", "17:00:00" ]

def get_next_alarm(times):
    now_dt = datetime.now()
    for t in times:
        # Convert the string time into a datetime object
        today_date = datetime.today() # create a date object
        alarm_time = datetime.strptime( t, '%H:%M:%S').time() # create the time object
        alarm_dt = datetime.combine(today_date, alarm_time) # create the datetime object
        # The first alarm_time we find that is in the future, is our next alarm
        if alarm_dt > now_dt:
            return alarm_dt
    return datetime.combine(datetime.today(), datetime.strptime( "23:59:59", '%H:%M:%S').time()) # Midnight as our failsafe

def clock_tick(*times):
    now_time = datetime.now()
    next_alarm_time = get_next_alarm(times)
    delta = next_alarm_time - now_time
    h = delta.seconds // 3600
    m = (delta.seconds % 3600) // 60
    s = delta.seconds % 60
    print(f"Time remaining is {h} hours {m:2} minutes {s:2} seconds.")
    threading.Timer(1, clock_tick, times).start()

if __name__ == "__main__":
    ticker = threading.Timer(1, clock_tick, alarms).start()
```
