# ArrayLists

There are two main types of arrays in Java. The classic static *array* has a size that is fixed at declaration. Once the memory space has been allocated, they can not be resized. The other type is known as *ArrayLists* and are a dynamically resizable construct available when the size of the array is not known in advance.

## Pre-requisite

This topic assumes you have an understanding of **arrays** and **object orientated programming**

# Array List

## Array List: Declaration

When instantiating an ArrayList, you can nominate the datatype to be contained by the array list or leave it unspecified (to allow for a potential mix of different data types).  There is an example of each below.

ArrayLists require: `import java.util.ArrayList;`

Example 1: Create an ArrayList specifying elements to be String

```java
ArrayList<String> alist = new ArrayList<String>();
alist.add("first");
alist.add("second");

for (String item: list) {
    System.out.println( item );
}
```

Example 2: Create an ArrayList without specifying element type

```java
ArrayList list = new ArrayList();
list.add( 3.14) );                      // Add a float
list.add( true );                       // Add a boolean
list.add( "Mixed data arrayList" );     // Add a string
list.add( 99 );                         // Add an integer

for (Object o : list) {
    if (o.getClass() == String.class) {
        System.out.println("The item is a string and it's value was "+o);
    } else if (o.getClass() == Integer.class) {
        System.out.println("The item is an integer and it's value was "+o);
    } else if (o.getClass() == Float.class) {
        System.out.println("The item is a float and it's value was "+o);
    } else if (o.getClass() == Boolean.class) {
        System.out.println("The item is a boolean and it's value was "+o);
    }
}
```

## Array List: Methods

* `list.add( o )` - Add object o to the end of the list
* `list.add( i, o )` - Add object o at position index i
* `list.get( i )` - Returns the object at position index i
* `list.push( o )` - Add object o to the end of the list
* `list.pop()` - Returns the last item on the list and removes it
* `list.remove( i )` - Remove object at index position i
* `list.size()` - The number of items in the list

## Array List: Convert to/from arrays

As arrays and ArrayLists both have beneifts over the other, the chances are high you are going to want to convert from one to the other at some time or another.

**Array to ArrayList**  

```java
int[] a = {1,2,3,5,7,11,13,17,19,23};
ArrayList alist = new ArrayList<>(Arrays.asList(a))
```

**ArrayList to Array**  

```java
String[] a = (String[])alist.toArray(new String[alist.size()]);
// or
int[] a = (int[])alist.toArray(new int[alist.size()]);
```


# Problem set: ArrayLists

For some introductory level questions, I recommend solving the problem sets on coding bat:

* [Array-1 coding.bat problems (no loops)](https://codingbat.com/java/Array-1)
* [Array-2 coding.bat problems (require 1 loop)](https://codingbat.com/java/Array-2)
* [Array-3 coding.bat problems (require 2 loops & complex logic)](https://codingbat.com/java/Array-3)

Be warned, a number of the questions in the main problem set are quite challenging for new programmers. Do not worry if you feel some of them are beyond you if you are at the beginning stags of learning to program. Revisit the questions you can't do after you have been programming consistently for about 12 months.

Note: Use ArrayLists as you feel best fits the problem. Do ensure you practice using a mix of both.

1. Write a program to sum all the items in a list.
2. Write a program to get the largest number from a list.
3. Write a program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
4. Write a program to remove duplicates from a list.
5. Write a function that takes two lists and returns True if they have at least one common member.
6. Write a program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']` Expected Output : `['Green', 'White', 'Black']`
7. Write a program to print the numbers of a specified list after removing even numbers from it.
8. Write a program to select an item randomly from a list, which is then removed from the original list so it can’t be re-drawn (just like a deck of cards scenario)
9. Write a program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
10. Given two lists, write a program to print the items that are not in both lists.
11. Write a program to append the items from one list to a second list.
12. Write a program for computing primes upto 1000. Hint: Google for the Sieve of Eratosthenes

For question 8, you may like to copy and paste the following as an array to use:

```java
String[] deck = {
    "A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️",
    "A♥️", "2♠️️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
    "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
    "A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️",
};
```
