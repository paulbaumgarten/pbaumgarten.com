# Java: Web requests

The following outlines how to perform a web request using the standard networking library. If you wish to use a 3rd party library, the [unirest Lightweight HTTP Request Client Libraries](http://unirest.io/java.html) look quite good. I'd recommend using the unirest library if you have to do any non-trivial requests such as post data, handling cookies, authentication, file upload/download etc.

There are generally going to be two parts to successfully achieving your web request.

1. Load the data from a web API (usually in JSON format).
2. Parse the data you received to extract the information you want.

There are a lot of competing Java JSON libraries around. I've used `org.json` which is available at:

* URL: [https://github.com/stleary/JSON-java](https://github.com/stleary/JSON-java)
* Maven: org.json:json

## Example

```java
package ch.isl.beyondbasics;

import java.time.LocalDateTime;
import java.time.Instant;
import java.time.ZoneId;
import java.net.*;  // URL reading 
import java.io.*;   // URL reading
import org.json.*;  // JSON parsing

public class WebRequestDemo {
    public static String makeRequest(String url) {
        String charset = java.nio.charset.StandardCharsets.UTF_8.name();
        String result = "";
        try {
            URL myURL = new URL(url);
            URLConnection connection = myURL.openConnection();
            connection.setRequestProperty("Accept-Charset", charset);
            connection.connect();
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            while ((inputLine = in.readLine()) != null)
                result = result + inputLine + "\n";
            in.close();
        } 
        catch (Exception e) { 
            System.out.println("*** EXCEPTION ***");
            System.out.println(e.getClass().toString());
            System.out.println(e.getMessage());
        } 
        return result;
    }

    public static void printNextSpaceXFlights(String jsonString) {
        // Fetch relevant details from JSON data
        JSONObject jo = new JSONObject(jsonString);
        String missionName = jo.getString("mission_name");
        long launchEpoch = jo.getLong("launch_date_unix");
        LocalDateTime ldt = LocalDateTime.ofInstant(Instant.ofEpochMilli(launchEpoch*1000), ZoneId.systemDefault());
        String launchDateTime = Integer.toString(ldt.getHour()) + ":" 
            + Integer.toString(ldt.getMinute()) + " on " 
            + Integer.toString(ldt.getDayOfMonth()) + " " 
            + ldt.getMonth().name() + ", " 
            + Integer.toString(ldt.getYear());
        String rocket = jo.getJSONObject("rocket").getString("rocket_name");
        String launchSite = jo.getJSONObject("launch_site").getString("site_name_long");
        String details = jo.getString("details");
        // Print the information
        System.out.println("The next scheduled SpaceX launch is:");
        System.out.println("Mission:          "+missionName);
        System.out.println("Launch date/time: "+launchDateTime);
        System.out.println("Launch site:      "+launchSite);
        System.out.println("Rocket:           "+rocket);
        System.out.println("Briefing:         "+details);
    }

    public static void printDogPicUrls(String jsonString) {
        // Fetch relevant details from JSON data
        JSONArray ja = new JSONArray(jsonString);
        for (int i=0; i<ja.length(); i++) {
            String datum = ja.getString(i);
            System.out.println(datum);
        }
    }

    public static void main(String[] args) {
        String url, result;

        // First demo... next SpaceX flight details
        url = "https://api.spacexdata.com/v2/launches/next";
        result = makeRequest(url);
        printNextSpaceXFlights(result);

        // Second demo... a list of dog pictures
        url = "http://shibe.online/api/shibes?count=5&urls=true&httpsUrls=false";
        result = makeRequest(url);
        printDogPicUrls(result);
    }
}
```

Remember to include the JSON library JAR file in your class path when compiling and executing

```bash
javac -d bin -cp bin:lib/* src/ch/isl/beyondbasics/WebRequestDemo.java
java -cp bin:lib/* ch.isl.beyondbasics.WebRequestDemo
```

## References

URL loading

* https://docs.oracle.com/javase/tutorial/networking/urls/index.html
* https://stackoverflow.com/a/2793153 - How to use java.net.URLConnection to fire and handle HTTP requests. Contains helpful tips for sending headers, making POST v GET requests, uploading files etc.
* http://hc.apache.org/httpcomponents-client-ga/quickstart.html - An alternative library that may be worth looking at

JSON parsing using `org.json`:

* JavaDocs: https://stleary.github.io/JSON-java/
* https://www.baeldung.com/java-org-json
* https://www.codevoila.com/post/65/java-json-tutorial-and-example-json-java-orgjson
* https://github.com/stleary/JSON-java
* http://theoryapp.com/parse-json-in-java/

Another library I was thinking of using was `org.json.simple`. I ended up not using it because it looks like it hasn't been updated in over 7 years, so I worry about it being a dead project.

* JavaDocs: http://alex-public-doc.s3.amazonaws.com/json_simple-1.1/index.html
* https://www.mkyong.com/java/json-simple-example-read-and-write-json/
* https://code.google.com/archive/p/json-simple/downloads
* https://www.geeksforgeeks.org/parse-json-java/

Finally, anotherone that could be worth looking at is 

* https://github.com/ralfstx/minimal-json

Note:

When searching for tutorials and documentation, be careful to search for "parsing" JSON. You will find a lot of Java tools that refer to serialising/deserialsing objects, or that make reference to pojo (plain-old-java-objects). For simple parsing of data received from a web api, these will be more complex than your needs.

