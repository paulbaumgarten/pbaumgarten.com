# Java: Numbers

Let's get started with programming by doing something very familiar to us all... doing simple mathematical calculations. Mathematical calculations are an essential part of any successful programming so being comfortable with the basics is a good idea.

## Demo: Simple arithmetic

Let's use Java as a calculator! Try the following commands. Hopefully they are all quite intuitive as to what they will do.

In your `javaprojects` folder, create the `src/ch/isl/basics/Exercise101.java` file as follows.

```java
package ch.isl.basics;

public class Exercise101 {
    public static void main(String[] args) {
        System.out.println( 2 + 2 );
        System.out.println( 1.5 + 2.25 );
        System.out.println( 7 - 2 );
        System.out.println( 3 * 4 );
        System.out.println( 10 / 2 );
    }
}
```

Open a console and compilte/execute:

```bash
$ javac -d bin src/ch/isl/basics/Exercise002.java
$ java -cp bin ch.isl.basics.Exercise002
```

Hopefully you got the outputs you would expect.  

Performing simple arithmetic is all well and good but in order to do anything remotely useful, we can't  manually write numbers for calculations; we need to use variables. 

A variable is a named memory location reserved for you to store values under that name. This will allow us to use the result from one calculation as the input for the next, etc.

Java is a **statically, strongly typed language** which means you must specify the **type** of data to be stored in any variable you create. For numbers, there are several data types available:

| data type | size | values |
| --------- | ---- | -------------------------- |
| boolean      | 1 bit | true, false |
| byte      | 8 bits | -128 to 127 |
| short     | 16 bits | -32,768 to 32,767 |
| int       | 32 bits | -2^31 to 2^31 - 1 |
| long      | 64 bits | -2^63 to 2^63 - 1 |
| float      | 32 bits | 1 bit sign, 8 bit exponent, 23 bits significant figures |
| double      | 64 bits | 1 bit sign, 11 bit exponent, 52 bit significant figures |

*Byte*, *short*, *int* and *long* are all **integer numbers**; that is they are whole numbers without any decimal component.

The easiest way to use decimals is with what are known as **floating point numbers**, which are *float* and *double* in Java. They store numbers capable of containing decimals by splitting the memory allocation into two main parts: one section stores a certain number of significant digits, the other section stores an exponnent. In other words, they work similar to how you could, in mathematics, write the decimal 0.13 as 13 multiplied by 10 raised to -2. The only catch is that the numbers are binary, so it would actually turn out to being 00001101 multiplied by 2 raised to -10 (hmmm... I think... see if you can double check my math on that)

Due to the issues involved of using base 2 for the significant component and the exponent, it means that floating point numbers regularly produce slightly weird results beyond the first few significant figures. They were designed especially for scientific calculations, where approximation errors are acceptable. They are not suitable where you need numbers that contain a lot of significant figures of accuracy (think currency storing values in thousands of dollars but also needing to store cents). In that case it is recommended to look at `BigDecimal` or to use a `long` and store the values in cents rather than dollars.

Example declarations of each type of number:

```java
boolean b = false;      // 1 bit
byte b = 1;             // 8 bits
short s = 2;            // 16 bits
int a = 1;              // 32 bits
long l = 1;             // 64 bits
float f = 1.0;          // 32 bits
double d = 1.0;         // 64 btts
int hex = 0xFF;         // hex FF = decimal 255
double uni = 13.772E9;  // 13.772 x 10^9 (age of the universe)
```

## Demo: Arithmetic with variables

In your `javaprojects` folder, create the `src/ch/isl/basics/Exercise102.java` file. Use the standard code outline you used previously, with the following as the content of the `main()` function.

```java
int a = 20;
int b = 6;
double c = 20;
double d = 6;
int answer1;
double answer2;

answer1 = a + b;                    // addition
answer2 = c + d;
System.out.println( answer1 );
System.out.println( answer2 );
answer1 = a - b;                    // subtraction
answer2 = c - d;
System.out.println( answer1 );
System.out.println( answer2 );
answer1 = a * b;                    // Multiplication
answer2 = c * d;
System.out.println( answer1 );
System.out.println( answer2 );
answer1 = a / b;                    // Integer division
answer2 = c / d;                    // Floating point division
System.out.println( answer1 );
System.out.println( answer2 );
answer1 = a % b;                    // Modulus (remainder)
answer2 = c % d;
System.out.println( answer1 );
System.out.println( answer2 );
```

Notice that there was a difference in the answer between the two divisions, even though we are performing the same operation on what might seem like the same numbers?  When you perform division with a pair of integers, this is more akin to the divison you may have learnt in elementary school. In this case, how many times does 6 go into 20? The answer is 3.  Performing the same operation with a pair of floating point numbers asks the question in the manner you are more used to from a calculator, 20 divided by 6 is 3.3333.

The modulus is the division remainder. If 6 goes into 20 three times, there is 2 left over. That 2 is the modulus.  One very common use of the modulus is for checking if a number is even or odd.

Beyond the simple arithmetic operations, Java has a large range of mathematical functions built in, however to use them we must first import them into our project. Java does not make all functions available to your program by default - this allows it to keep your outputted program file size smaller by only including the functionality your program actually needs. So, to use the functions in the Math library as we are about to, immediately after the line containing our package name we specify `import java.lang.Math;`.

## Demo: Importing and using the Math library

As this is the first time we are doing an import, I'll provide you the full code example. 

```java
package ch.isl.basics;
import java.lang.Math;

public class Exercise103 {
    public static void main(String[] args) {
        double a = 20;
        double b = 6;
        double answer;

        answer = Math.pow(a,b);         // Exponential
        System.out.println( answer );
        answer = Math.sqrt(a);          // Square root
        System.out.println( answer );
        answer = Math.round( 13.4 );    // Rounding
        System.out.println( answer );
        answer = Math.abs( -13 );       // Absolute value
        System.out.println( answer );
        answer = Math.random();         // A random number between 0 and 1
        System.out.println( answer );
    }
}
```

There are a whole range of useful functions in the Math library.  Here are some of the more useful ones you are likely to use.

* `Math.pow( base, exponent )` - Perform exponential calculation, *base* raised to *exponent*.
* `Math.sqrt( num )` - What is the square root of *num*?
* `Math.round( num )` - Round *num* to the nearest integer value
* `Math.floor( num )` - Truncate any decimals off of *num* down to the nearest integer value
* `Math.abs( num )` - What is the absolutele value of *num*?
* `Math.round()` - Generate a random number between 0 and 1
* `Math.max( a, b )` - Which number is larger out of *a* or *b*?
* `Math.min( a, b )` - Which number is smaller out of *a* or *b*?
* `Math.PI` - The value of the mathematical constant PI, ie: 3.1415.
* `Math.E` - The value of the mathematical constant E, ie: 2.7183.
* `Math.sin( num )` - What is the sine value of *num*? (answers in radians)
* `Math.cos( num )` - What is the cosine value of *num*? (answers in radians)
* `Math.tan( num )` - What is the tangent value of *num*? (answers in radians)
* `Math.asin( num )` - What is the inverse sine value of *num*? (assumes input of radians)
* `Math.acos( num )` - What is the inverse cosine value of *num*? (assumes input of radians)
* `Math.atan( num )` - What is the inverse tangent value of *num*? (assumes input of radians)
* `Math.hypot( a, b )` - Given sides of length *a* and *b*, what is the hypotenous?
* `Math.toDegrees( r )` - Convert *r* radians to degrees
* `Math.toRadians( d )` - Convert *d* degrees to radians

## Demo: User input of nnumbers

One last little thing before I assign you some exercises to use these functions, let's find a way to prompt the user for input so we can make an intereactive program to calculate results.

1. Create the reader variable using `java.util.Scanner reader = new java.util.Scanner(System.in);`. Do this only once at the start of your function.
2. Whenever you want to prompt, use `val = reader.nextDouble();` assuming that `val` is a previously declared double.

```java
java.util.Scanner reader = new java.util.Scanner(System.in);
double base, expon, answer;

System.out.println("Exponentials calculator");
System.out.print("Base: ");
base = reader.nextDouble();
System.out.print("Exponent: ");
expon = reader.nextDouble();
answer = Math.pow(base, expon);
System.out.println( answer );
```

## Problem set

The following questions assume you will use variables as the inputs into the problem, so the problems can re-caclulate solutions by changing the value assigned to the variable. You should also print the given information in your answer.

1. For any given number, extract the 10s digit. For example, `The tens digit in 1234 is 3.`
2. Area of a right angled triangle calculator. Given values for `base` and `height`, print the area.
3. For any two digit number, swap the position of the digits. For instance, `79` becomes `97`.
4. For any three digit number, print the sum of the three digits. For instance `273` becomes `12` (2+7+3)
5. For any given year, print the century that year belongs to. Remember that 1999 and 2000 were the 20th century, whereas 2001 was the beginning of the 21st century.
6. Given a number representing the number of seconds since midnight, print the time in 24hour clock format. For example `70500` seconds should print a time of `19:35`.
7. Area of a non-right angled triangle calculator. Given values for length `a`, length `b` and angle in degrees `C`, return the area of the triangle (remember you will have to convert degrees to radians first).
8. For any given values for `a`, `b` and `c`, will provide the solutions to the quadratic formula (you may assume both solutions are required). Be careful with your order of precedence. Here is an example solution set for testing: If `y=2x^2-4x-10` then the solutions are `3.44949` and `-1.44949`.
