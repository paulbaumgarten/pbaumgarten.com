# Java: Functions
We have been using a lot of various functions that exist within Java already but haven't created any of our own, other than using `main()`.

Functions are a useful way of abstracting complexity in our project. Functions will generally require one or more inputs, and then provide a returning result.

Functions are blocks of code that you assign a name to. You can use that name to easily run that code again whenever you need.

Functions are very useful for separating common tasks out from your main code. It allows you to avoid repeating yourself all the time which makes your code easier to maintain. Tasks like reading from a file, saving to a file, etc are all ideally suited to being chopped off into a separate function. 

> Think of an Icecreamary
> 
> Lots of different possible flavours, toppings, numbers of scoops, choice of waffle or regular cone, etc.
>
> One person could order a double scoop of chocolate fudge and vanilla on a waffle cone, where as the next customer might ask for a cup of raspberry sorbet with nut sprinkles. The salesperson calculates the cost for each and advises each custoemr on the price. In order to calculate that cost there are a number of inputs (number of scoops, type of cone, etc) and an output (price). How it is actually calculated is not important, provided it is trustworthy and works reliably. 
>
> In this way a function can provide a "black box" model through which we can create an abstraction to represent our problem. 
>
> Programmers need to know how to (a) use other peoples abstractions and (b) be able to create their own. For now, the abstraction we are concerned with is creating a function.


## Functions

Convert the mathematical function `A = π r^2` to Java:

```java
public static double areaOfCircle( double radius ) {
    return Math.PI * radius * radius;
}
```

*We'll discuss keyword by keyword first. Don't code it yet*

* `public` - is known as an **access modifier**. We'll discuss the role of access modifiers more when we look at classes. There are four access modifiers in Java: *default* (ie: when not explicitly specified), *private*, *protected*, and *public*. To keep things simple while you are learning we will limit ourselves to only using *public* and *private*. See the access modifier section in classes for more information about how these work, for now just make sure you specify it when you create a function.
* `static` - again understanding the function of this keyword will be further explained in the classes section (the presence of this keyword means that the function belongs to the class rather than an object). Again, until we start building classes and objects, have this keyword present when creating a function.
* `double` - this is the data type that the function will return. Functions can provide a value back to the code that calls it, and the function must specify what type of data it will return.
* `areaOfCircle` - finally, this is the name of our function.
* `(double radius)` - immediately following the name of the function is the list of parameter values we will expect to be supplied to the function. In this case, we are expecting one value of type double, which we will refer to internally within the function via the name radius. This name does not have any relation to any variable that may be used outside the function. To accept more than one parameter, we comma separate them.
* `{ .... }` - The code to be executed by our function is enclosed within the braces.
* `return` - This is where we specify the value to be returned to the code that called the function. Once Java encounters a return statement, it will exit the function regardless of any further code you may have written. Your function must provide a return value unless you specify the function datatype as `void` (like we do with main).


## Writing your 1st function

```java
package com.pbaumgarten.basics;
import java.lang.Math;
import java.util.Scanner;

public class Functions01 {

    public static double areaOfCircle( double radius ) {
        return Math.PI * radius * radius;
    }

    public static void main(String[] args) {
        // Define our variables
        Scanner reader = new Scanner(System.in);
        double r, answer;
        // Query the user
        System.out.print("Radius: ");
        r = reader.nextDouble();
        // Execute the function we created
        answer = areaOfCircle(r);
        // Print the result
        System.out.println( "The area of this circle is: "+answer );
    }
}
```

## Writing your 2nd function

This next example illustrates two ideas:

* Creating a function that requires two parameters.
* Importing a function we created elsewhere into the current class file. We will reuse our previous `areaOfCircle` function without having to rewrite it. This is one of the coolest reasons to write functions, we can start re-using previous code!

## Writing your 2nd function

```java
package com.pbaumgarten.basics;
import java.lang.Math;
import java.util.Scanner;

public class Functions02 {

    public static double areaOfCircle( double radius ) {
        return Math.PI * radius * radius;
    }

    public static double areaOfCylinder(double radius, double length) {
        return length * areaOfCircle(radius);
    }

    public static void main(String[] args) {
        Scanner keyb = new Scanner(System.in);
        double rad, len, answer;
        System.out.println("Surface area of cylinder calculator");
        System.out.print("Radius: ");
        rad = keyb.nextDouble();
        System.out.print("Length: ");
        len = keyb.nextDouble();
        answer = areaOfCylinder(rad,len);
        System.out.println( "The surface area of this cylinder is: "+answer );
    }
}
```

## Functions for user input validation

Functions can be a handy way to require the user to comply with our wishes to enter information in a particular manner. By the time we write the checking/validation code and the loop, user input checks can run to several lines, and it would be quite common within a simple program to want to validate the same style of input several times. Functions make a handy way to reuse code for this purpose.

```java
public static String confirm( String prompt ) {
    boolean loop = true;
    String response = ""
    java.util.Scanner keyb = new java.util.Scanner(System.in);
    while (loop) {
        System.out.println( prompt );
        response = keyb.nextLine();
        if (response.equals("y") || response.equals("n")) {
            loop = false;
        } else {
            System.out.println("Only a 'y' or 'n' character are accepted. Please try again.");
        }
    }
    return response;
}
```


# Problem set

1. Create a function `areaRightAngledTriangle(double base, double height)` that returns the calculated area.

2. Create a function `areaNonRightAngledTriangle(double base, double height, double angle)` that returns the calculated area (remember you will need to convert the angle to radios before using it with the sine function).

3. Create a user input validation function that requires the input of a number.

4. Create a user input validation function that requires the input of a phone number (so `+`, spaces and `-` characeters are permitted).

5. Create a user input validation function that requires the input of a date in the `dd/mm/yyyy` format.

6. *(return to this one after we've done arrays)* Create a user input validation function that accepts an array of strings as the parameter and presents them to the user as a list of menu choices, requiring the user to enter a number cooresponding to a valid choice before proceeding. For example if the code to run the funciton was....

```java
String[] menu = {"Open file", "Save file", "Quit program"};
choice = menuPicker( menu );
System.out.println("You choose option "+choice);
```

The output could look like...

```text
Your choices are:
1. Open file
2. Save file
3. Quit program
Please enter a number from 1 to 3:
```


