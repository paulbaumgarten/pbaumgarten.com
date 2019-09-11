# Java: Casting

Because variables in Java are strictly typed, a common task is to want to convert the value in one variable to that of another type. For instance, if we have a String that contains the text of a number, we need to convert it to a numeric variable before we can perform calculations on it.  This process of conversion is known as **casting**.

The following shows you how to cast between the common data types.

```java
// Given these variables
byte b = 1;
short s = 2;
int i = 3;
long l = 4;
float f = 5.0F;
double d = 6.0;
String s1 = "4";
String s2 = "5.3";
char c = '7';                               // Single quotes for char

// To integers
int num1 = Integer.parseInt( s1 ); 
int num2 = Integer.parseInt( s2 );          // RUN TIME ERROR
int num3 = (int)f;
int num4 = (int)d;
int num5 = (int)l;
int num6 = (int)c;

// To long
long l1 = Long.parseLong( s1 ); 
long l2 = Long.parseLong( s2 );             // RUN TIME ERROR
long l3 = (long)f;
long l4 = (long)d;
long l5 = (long)l;
long l6 = (long)c;

// To float
float fl1 = Float.parseFloat( s1 ); 
float fl2 = Float.parseFloat( s2 ); 
float fl3 = (float)i;
float fl4 = (float)l;
float fl5 = (float)d;
float fl6 = (float)c;

// To doubles
double do1 = Double.parseDouble( s1 ); 
double do2 = Double.parseDouble( s2 ); 
double do3 = (double)i;
double do4 = (double)l;
double do5 = (double)d;
double do6 = (double)c;

// To strings
String str1 = Integer.toString( i ); 
String str2 = Float.toString( f ); 
String str3 = Double.toString( d ); 
String str4 = Long.toString( l ); 
String str5 = Character.toString( c );
```

## Questions

* What is printed?

```java
double d = 78.1; 
int fg = (int)d;
System.out.println(fg);
```

* What is printed?

```java
int p = 3;
double d = 10.3;
int j = (int)5.9;
System.out.println(p + p * d – 3 * j);
```

* The following code stores a 20 in the variable j: `double j = 61/3;`. What small change can you make to this single line of code to make it print the “real” answer to the division?


