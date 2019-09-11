# Java: Comparing values

The power of programming comes from letting the computer do work for us. To do that it needs to make decisions. We can have Java make decisions on the basis of comparing one value to another. These comparisons should always generate a boolean result, that is *true* or *false*. We can then instruct Java to execute code based on whether a comparison is true or false.

## Numeric comparisons

To compare the values of any numeric values or variables, the following operators exist:

* `(a == b)` ... is equal to
* `(a != b)` ... is not equal to
* `(a > b)` ... greater than
* `(a >= b)` ... greater than or equal to
* `(a < b)` ... less than
* `(a <= b)` ... less than or equal to

Note that *a* and *b* can either be a value or a variable, and that the surrouding set of parenthesis is required.

For example

```java
boolean result;
int a = 10, b = 3;
result = ( a == b );
System.out.println( result );
result = ( a != b );
System.out.println( result );
result = ( a > b );
System.out.println( result );
result = ( a < b );
System.out.println( result );
```

Take careful note of the difference in punctuation between setting a value to a variable, and comparing two values! Setting a variable to a given value uses the single equal sign `=` whereas comparing two values or variables uses the double equal sign `==`.

## String comparisons

There are a variety of functions suitable for comparing the values of strings as the following illustrates:

```java
java.util.Scanner reader = new java.util.Scanner(System.in);
System.out.print("Type string 1: ");
String s1 = reader.nextLine();
System.out.print("Type string 2: ");
String s2 = reader.nextLine();

System.out.println( s1.equals(s2) ); // also Objects.equals(s1, s2)
System.out.println( s1.compareTo(s2) );
System.out.println( s1.contains(s2) );
System.out.println( s1.endsWith(s2) );
System.out.println( s1.startsWith(s2) );
System.out.println( s1.isEmpty() );
```

You will notice they all return boolean results except `.compareTo()` which returns an integer result indicating how closely the two strings compare or differ. Specifically, it will return:

* zero when string values match
* negative when the parent object (s1) is alphabetically before the parameter (s2)
* positive when the parent object (s1) is alphabetically after the parameter (s2)
* the size of the positive or negative number indicates the value of number of characters different. For example `"a".compareTo("d")` will return -3 because the letter *a* is three values before the letter *d*.

## Multiple comparisons

Boolean logic can be used to diasy chain multiple comparisons into one instruction.

* The AND operator is the double ampersand `&&`.
* The OR operator is the double pipe `||`.
* The NOT operator is the exclaimation `!`.

The following is a valid example:

```java
int a = 13;
int b = 4;
int c = 10;
boolnea result;

result = ( (a > b) && (a < c) );
result = ( (a > b) || (a < c) );
result = ( (a != b) && (a < c) || (b == c) );
```

Where you are uncertain about order of precedence, it is recommended to use an additional set of parenthesis to enforce your intended outcome.

## Ternary operator

You may see a this used when searching online documentation, so I wanted to briefly show it here. It is known as the ternary operator.

The ternary operator allows you to set a resulting value based on whether or not a comparison condition is true. For example, if we didn't have the `Math.max()` function, we could use the tenary operator to easily identify the larger of two numbers...

```java
int largerOfTheTwo = (a>b) ? a : b;
```

The general rule for the ternary operator is:

```java
result = (condition) ? result_if_true : result_if_false ;
```

## Problem set

The following problems all use the following code:

```java
int i = 10
int j = 3;
boolean true_false;
```

What will be the value of `true_false` after each comparison?

1. true_false = ( j > i );
2. true_false = ( i > j );
3. true_false = ( i= = j );
4. true_false = ( (j<=i)||(j>=i) );
5. true_false = ( (i>j)&&(j==0) );
6. true_false = ( (j<50)||(j!=33) );
7. true_false = ( !(j>=0)||(i<=50) );
8. true_false = ( !(! (!true)) );
9. true_false = ( 5 < = 5 );
10. true_false = ( j != i );
11. What is returned by the following expression? (Recall that the precedence order of logical operators is `!`, `&&`, and finally `||`.)

`!( (2>3) | | (5= =5) && (7>1) && (4<15) | | (35<=36) && (89!=34) )`

(Exercises adapted from Blue Pelican Java)

