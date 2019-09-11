# Java: Exceptions

An exception is a critical event that should be foreseeable by a programmer that Java expects you to program a response to. Examples situations include:

* Attempting to divide by zero
* Attempting to cast a string to an integer when it doesn't contain a number
* Attempting to read a file beyond it's end point
* Attempting to write to a file that is read-only, or has a full disk, or has other issues
* Attempting to access an array beyond the number of elements it contains

Let's make an example:

```java
package ch.isl.basics;

public class ExerciseB01{
    public static void main( String args[] ) {
        java.util.Scanner reader = new java.util.Scanner(System.in);

        System.out.print("Input a number:");
        String s1 = reader.nextLine();
        int i1 = Integer.parseInt( s1 );

        System.out.print("Input another number:");
        String s2 = reader.nextLine();
        int i2 = Integer.parseInt( s2 );

        // Perform division
        int result = i1/i2;

        // Output result
        System.out.println(result);
    }
}
```

The above code will compile and execute just fine until....

* What happens if you enter "ten" as one of the inputs?
* What happens if you enter "0" as the second input?

The first should give you the message, `Exception in thread "main" java.lang.NumberFormatException`.

The second should give you the message, `Exception in thread "main" java.lang.ArithmeticException: / by zero`

Java expects us to catch these exceptions so our program can deal with them gracefully instead of causing the program to fail. For instance, with the datatype conversion, we could prompt the user to re-enter their input.  The following illustrates how to fix it through the simple use of `try` and `catch`.

```java
package ch.isl.basics;

public class ExerciseB02{
    public static void main( String args[] ) {
        java.util.Scanner reader = new java.util.Scanner(System.in);

        try {
            // Input 1st number
            System.out.print("Input a number:");
            String s1 = reader.nextLine();
            int i1 = Integer.parseInt( s1 );
            // Input 2nd number
            System.out.print("Input another number:");
            String s2 = reader.nextLine();
            int i2 = Integer.parseInt( s2 );
            // Perform division
            int result = i1/i2;
            // Output result
            System.out.println(result);
        } catch(Exception e) {
            System.out.println("An exception happened.");
            System.out.println("Exception type: "+e.getClass().toString());
            System.out.println("Message:        "+e.getMessage());
        }
    }
}
```

A better solution is to check for the type of exception so a more meaningful message can be given to the user.

```java
package ch.isl.basics;

public class ExerciseB03{
    public static void main( String args[] ) {
        java.util.Scanner reader = new java.util.Scanner(System.in);

        try {
            // Input 1st number
            System.out.print("Input a number:");
            String s1 = reader.nextLine();
            int i1 = Integer.parseInt( s1 );
            // Input 2nd number
            System.out.print("Input another number:");
            String s2 = reader.nextLine();
            int i2 = Integer.parseInt( s2 );
            // Perform division
            int result = i1/i2;
            // Output result
            System.out.println(result);
        } catch(NumberFormatException e) {
            System.out.println("One of your inputs could not be converted to an integer");
        } catch(ArithmeticException e) {
            System.out.println("You attempted to divide by zero. I can't do the impossible!");
        } catch(Exception e) {
            System.out.println("An unknown exception happened.");
            System.out.println("Exception type: "+e.getClass().toString());
            System.out.println("Message:        "+e.getMessage());
        }
    }
}
```

Not sure what the likely exceptionis are called? The simple way is to not catch for them, run your code in a way to generate the exception, and then Java will tell you the exception names!

Finally, a more complete solution would be to actually check for exceptions at each point they could occur and to provide the user a way to fix their inputs if possible. The following shows this.

```java
package ch.isl.basics;

public class ExerciseB04{
    public static void main( String args[] ) {
        java.util.Scanner reader = new java.util.Scanner(System.in);
        int i1, i2;

        // Input and convert first number
        while (true) {
            try {
                System.out.print("Input a number:");
                String s1 = reader.nextLine();
                i1 = Integer.parseInt( s1 );
                break;  // break out of the while loop
            } catch (NumberFormatException e) {
                System.out.println("What you entered could not be converted to an integer. Please try again.");
            }
        }

        // Input and convert second number
        while (true) {
            try {
                System.out.print("Input another number:");
                String s2 = reader.nextLine();
                i2 = Integer.parseInt( s2 );
                break;  // break out of the while loop
            } catch (NumberFormatException e) {
                System.out.println("What you entered could not be converted to an integer. Please try again.");
            }
        }

        // Perform division
        try {
            int result = i1/i2;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Can not divide by zero");
        }

    }
}
```
