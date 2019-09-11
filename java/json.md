# JSON as Data (Java)

There are a lot of competing Java JSON libraries around. I've used `org.json` which is available at:

* URL: [https://github.com/stleary/JSON-java](https://github.com/stleary/JSON-java)
* Maven: org.json:json

When searching for tutorials and documentation, be careful to search for "parsing" JSON. You will find a lot of Java tools that refer to serialising/deserialsing objects, or that make reference to pojo (plain-old-java-objects). For simple parsing of data received from a web api, these will be more complex than your needs.

Refererences:

* JavaDocs: https://stleary.github.io/JSON-java/
* https://www.baeldung.com/java-org-json
* https://www.codevoila.com/post/65/java-json-tutorial-and-example-json-java-orgjson
* https://github.com/stleary/JSON-java
* http://theoryapp.com/parse-json-in-java/

Sample code

```java
package com.pbaumgarten.beyondbasics;

import org.json.*;  // JSON parsing

class JSONDemo {

    public boolean saveData(String filename) {
        // Convert the ArrayList of Person objects into a JSONArray of JSONObjects
        JSONArray ja = new JSONArray();
        for (Person p : people) {
            JSONObject jo = new JSONObject(p);
            ja.put(jo);
        }
        // Save the JSONArray to a text file
        try {
            FileWriter fw = new FileWriter(filename);
            PrintWriter output = new PrintWriter(fw);
            output.println( ja.toString() );
            output.close();
            fw.close();
            return true;
        } catch(Exception e) {
            System.out.println("[saveData] error saving "+filename);
            return false;
        }
    }

    public ArrayList<Person> loadData(String filename) {
        StringBuilder sb = new StringBuilder();
        ArrayList<Person> results = new ArrayList<Person>();
        try {
            // Load the JSON file as String data
            File f = new File(filename);
            Scanner reader = new Scanner(f);
            while (reader.hasNextLine()) {
                sb.append(reader.nextLine());
            }
            reader.close();
            // Create a JSONArray from the String
            JSONArray ja = new JSONArray(sb.toString());
            // Iterate over the JSONObjects within the JSONArray
            for (int i=0; i< ja.length(); i++) {
                JSONObject o = ja.getJSONObject(i);
                // Use each JSONObject to create a Person object
                Person p = new Person(
                    o.getString("name"), 
                    o.getString("email"), 
                    o.getString("phoneNumber"), 
                    o.getString("dateOfBirthString")
                );
                // Add the Person object to the ArrayList of people
                results.add(p);
            }
            return results;
        } catch(Exception e) {
            System.out.println("[loadData] error loading "+filename);
            return null;
        }
    }

    public static void main(String[] args) {
        // TO DO
    }
}
```
