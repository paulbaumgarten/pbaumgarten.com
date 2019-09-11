# Java: Strings

A *string* is the programming term for text. More properly it can be thought of as *a string of characters*. We've already used strings whenever we've used the double quote enclosed text in the println() function. We can also use strings with variables. The string variable in Java is defined with a capitalised **String**.

## Demo: Strings

A simple example program that uses strings and performs common operations on them.

```java
String s1 = "May the force be with you!";
String s2 = "Always two there are";

System.out.println( s1.length() );
System.out.println( s2.length() );

System.out.println( s1.charAt(0) );
System.out.println( s1.charAt(1) );
System.out.println( s1.charAt(1) + 1 );
System.out.println( s1.charAt(2) );

System.out.println( s2.indexOf(" ") );
System.out.println( s2.lastIndexOf(" ") );
System.out.println( s1.substring(8, 12) );
System.out.println( s2.replace("two", "three") );
System.out.println( s1.toUpperCase() );
System.out.println( s2.toLowerCase() );

String s3 = s1 + " " + s2; 	// concatenation
System.out.println( s3 );
```

## Demo: User input: Strings

To input from the user some text as a string, it works very similar to numbers except we use the `nextLine()` function.

```java
java.util.Scanner reader = new java.util.Scanner(System.in);

System.out.print("What is your full name? ");
String fullName = reader.nextLine();
System.out.println("Hello, "+n);
int space = fullName.lastIndexOf(" ");
String givenName = fullName.substring(0, space);
String familyName = fullName.substring(space+1, fullName.length());
System.out.println("Your given name(s) are "+givenName);
System.out.println("Your family name is "+familyName);
```

## Problem set

1. For any string that consists of exactly two words with one space separating them, swap the two words around. For example: Given the string `Hello world!`, have the program print `world! Hello`.
2. Given a sentence input, return how many words are in the sentence. For example, `The quick brown fox jumps over the lazy dog.` is `9` words.
3. Given a string input of a date in format, `dd/mm/yyyy`, print an output advising the current day, month and year number.
4. Given a string, return a new string made of 3 copies of the last 2 chars of the original string. Assume the input string length will be at least 2 characters. For example, the string "Hello" should be result in "lololo".
5. Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
6. Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
7. Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1. For example, strings "Hello" and "There" should result in "ellohere".
8. How would you print the following? `All "good" men should come to the aid of their country.` (ie: how to print the double quote character)
9. Write code that will produce the following printout using only a single print() function call. 

```txt
Hello
Hello again
```
