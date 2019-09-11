# Java: Hashmaps

Hashmaps are used for key-value storage of objects by Java.

Let's create a simple `PersonDemo` class to use in our example...

```java
package ch.isl.beyondbasics;

public class PersonDemo {
    private String givenName;
    private String familyName;
    private String email;

    PersonDemo(String givenName, String familyName, String email) {
        this.givenName = givenName;
        this.familyName = familyName;
        this.email = email;
    }

    public String toString() {
        return givenName+" "+familyName+" ("+email+")";
    }
}
```

Here is the example code using the HashMap...

```java
package ch.isl.beyondbasics;
import java.util.HashMap;
import java.util.Iterator;

public class HashMapDemo {
    public static void main(String[] args) {
        // Instantiate a HashMap
        // * The key will be a String
        // * The value will be a PersonDemo
        HashMap<String, PersonDemo> people = new HashMap<String, PersonDemo>();

        // Putting objects where they exist as variables
        PersonDemo me = new PersonDemo("Paul","Baumgarten","pbaumgarten@isl.ch");
        people.put("me", me);

        // Putting objects that are not separate variables
        people.put("batman", new PersonDemo("Bruce","Wayne","bruce@wayne-enterprises.com"));
        people.put("superman", new PersonDemo("Clark","Kent","clark@planet.com"));
        people.put("wonderwoman", new PersonDemo("Diana","Prince","diana@gmail.com"));

        // Iteration
        System.out.println("Iterating through HashMap collection:");
        for (Object o : people.values()) {
            System.out.println( " * " + ((PersonDemo)o).toString() );
        }

        // Getting an individual record
        System.out.println("Getting an individual item from HashMap:");
        PersonDemo p = (PersonDemo)people.get("me");
        System.out.println( p.toString() );
    }
}
```

More information:

* https://www.geeksforgeeks.org/java-util-hashmap-in-java/

