# Java: Linked lists

For some bizarre reason, the built in LinkedList class in Java does not actually implement a pure Linked List structure. If you require an actual linked list with `.next()` style functionality, you'll need to roll your own.

Using the same `personDemo` class we used in the HashMapDemo.

```java
package ch.isl.beyondbasics;
import java.util.LinkedList;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<PersonDemo> people = new LinkedList<PersonDemo>();

        PersonDemo me = new PersonDemo("Paul","Baumgarten","pbaumgarten@isl.ch");
        people.push(me);
        people.push(new PersonDemo("Bruce","Wayne","bruce@wayne-enterprises.com"));
        people.push(new PersonDemo("Clark","Kent","clark@planet.com"));
        people.push(new PersonDemo("Diana","Prince","diana@gmail.com"));

        while (! people.isEmpty() ) {
            PersonDemo person = people.pop();
            System.out.println( person.toString() );
        }
    }
}
```

To create your own actual LinkedList, see my teaching notes for the DP Computer Science course introducing the LinkedList.

* [https://pbaumgarten.com/dp-compsci/unit-5/#linked-lists](https://pbaumgarten.com/dp-compsci/unit-5/#linked-lists)

More information on the built in Java object:

* [https://www.geeksforgeeks.org/linked-list-in-java/](https://www.geeksforgeeks.org/linked-list-in-java/)

