# Java: Dates & times

Sooner or later every programmer needs to deal with times and dates. Knowing the appropriate functions for the task can be a mind numbing experience, so it's very handy to heep a reference guide nearby! The following is my attempt. Please suggest improvements.

The following is for Java 8 onwards and comes from https://www.tutorialspoint.com/java8/java8_datetime_api.htm

Prior to Java 8, it is recommended to use a 3rd party class such as http://www.joda.org/joda-time/

```java
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.LocalDateTime;
import java.time.Month;

// Get the current date and time

LocalDateTime ldt = LocalDateTime.now();
System.out.println("Current DateTime: " + ldt);         // Current DateTime: 2014-12-09T11:00:45.457

// Get properties of the date/time

LocalDate d = ldt.toLocalDate();                        // eg: 2019-01-01
int y = ldt.getYear();                                  // eg: 2019
String m = ldt.getMonth().name();                       // eg: JANUARY
int m = ldt.getMonthValue();                            // eg: 1
int day = ldt.getDayOfMonth();                          // eg: 1
String dow = ldt.getDayOfWeek().name();                 // eg: TUESDAY
int h = ldt.getHour();                                  // eg: 23
int min = ldt.getMinute();                              // eg: 59
int s = ldt.getSecond();                                // eg: 59

// Take the current values for from the original LocalDateTime except for those you are manually overriding.

LocalDateTime ldt2 = ldt.withDayOfMonth(10).withYear(2012);
System.out.println("date2: " + date2);                      // date2: 2012-12-10T11:00:45.457

LocalDate date3 = LocalDate.of(2014, Month.DECEMBER, 12);   // 12 december 2014
System.out.println("date3: " + date3);                      // date3: 2014-12-12

LocalTime date4 = LocalTime.of(22, 15);                     // 22 hour 15 minutes
System.out.println("date4: " + date4);                      // date4: 22:15

LocalTime date5 = LocalTime.parse("20:15:30");              // parse a string
System.out.println("date5: " + date5);                      // date5: 20:15:30
```

## Time zones

```java
import java.time.ZonedDateTime;
import java.time.ZoneId;

// Get the current date and time
ZonedDateTime date1 = ZonedDateTime.parse("2007-12-03T10:15:30+05:30[Asia/Karachi]");
System.out.println("date1: " + date1);              // date1: 2007-12-03T10:15:30+05:00[Asia/Karachi]

ZoneId id = ZoneId.of("Europe/Paris");
System.out.println("ZoneId: " + id);                // ZoneId: Europe/Paris

ZoneId currentZone = ZoneId.systemDefault();
System.out.println("CurrentZone: " + currentZone);  // CurrentZone: Etc/UTC
```

## Difference between two dates/times

With Java 8, two specialized classes are introduced to deal with the time differences −

* Period − It deals with date based amount of time.
* Duration − It deals with time based amount of time.

```java
import java.time.temporal.ChronoUnit;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Duration;
import java.time.Period;

//Get the current date
LocalDate date1 = LocalDate.now();
System.out.println("Current date: " + date1);

//add 1 month to the current date
LocalDate date2 = date1.plus(1, ChronoUnit.MONTHS);
System.out.println("Next month: " + date2);

// Period between to dates
Period period = Period.between(date2, date1);
System.out.println("Period: " + period); // P-1M

// Duration between to times
LocalTime time1 = LocalTime.now();
Duration twoHours = Duration.ofHours(2);
LocalTime time2 = time1.plus(twoHours);
Duration duration = Duration.between(time1, time2);
System.out.println("Duration: " + duration); // PT2H
```

## Unix time / Epoch time

```java
import java.time.LocalDateTime;
import java.time.LocalDate;
import java.time.Instant;
import java.time.ZoneId;

// Current UTC unix time in seconds
long unixTime = System.currentTimeMillis() / 1000L;

// Convert epoch time into a LocalDateTime
LocalDateTime ldt = LocalDateTime.ofInstant(Instant.ofEpochMilli(unixTime*1000), ZoneId.systemDefault());

// A "new" Java 8 function that does the same thing
// import java.time.Instant
Instant instant = Instant.ofEpochMilli(millis);

// Take an existing LocalDate object and get its epoch time
LocalDate date = ...;
ZoneId zoneId = ZoneId.systemDefault(); // or: ZoneId.of("Europe/Oslo");
long epoch = date.atStartOfDay(zoneId).toEpochSecond();

// Take an existing LocalDateTIme object and get its epoch time
LocalDateTime time = ...;
ZoneId zoneId = ZoneId.systemDefault(); // or: ZoneId.of("Europe/Oslo");
long epoch = time.atZone(zoneId).toEpochSecond();
```

## Convert from the old java.util.Date object to the new version

```java
import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.util.Date;
import java.time.Instant;
import java.time.ZoneId;

//Get the current date
Date currentDate = new Date();
System.out.println("Current date: " + currentDate);

//Get the instant of current date in terms of milliseconds
Instant now = currentDate.toInstant();
ZoneId currentZone = ZoneId.systemDefault();

LocalDateTime localDateTime = LocalDateTime.ofInstant(now, currentZone);
System.out.println("Local date: " + localDateTime);

ZonedDateTime zonedDateTime = ZonedDateTime.ofInstant(now, currentZone);
System.out.println("Zoned date: " + zonedDateTime);
```


```
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.Period;

public class Automobile {
   private String registration;
   private LocalDate purchaseDate;

   Automobile(String registration, String purchaseDate) {
      System.out.println("Automobile constructor is executing...");
      this.registration = registration;
      this.purchaseDate = LocalDate.parse(purchaseDate, DateTimeFormatter.ofPattern("dd/MM/yyyy"));
   }

   public String getRegistration() {
      return this.registration;
   }

   public int getAge() {
      LocalDate today = LocalDate.now();
      Period period = Period.between(this.purchaseDate, today);
      return period.getYears();
   }

   public static void main(String[] args) {
      Automobile car = new Automobile("VD-1234", "01/07/2010");
      System.out.println("Your car is " + car.getAge() + " years old");
   }
```