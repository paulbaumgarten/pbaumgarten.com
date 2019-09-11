# Iteration ("while", "for")

Another term for iteration is repetition. It is where we ask Java to repetitively execute a block of code while a condition is being met. There are two main types, the `while` loop and the `for` loop.

The basic syntax of a "while loop" is as follows:

```java
while ( comparison ) {
   instructions();
}
```

The following is a simple example of the `while()` loop that will count from 0 to 9.

```java
int a = 0;
while ( a < 10 ) {
   System.out.println( a );
   a = a + 1;
}
```

The basic syntax of a "for loop" is:

```java
for ( initialization ; comparison ; iterationIncrementer ) { 
   instructions();
}
```

Here is the `for()` loop counting from 0 to 9

```java
for (int i=0 ; i<10 ; i=i+1 ) {
   System.out.println( i );
}
```

## Problem set: Mixed

## Problem set - Truth

What range of inputs is required for each of the following to return True

```python
a = (int)input("Enter a number:")
truthy = 0 < a and 100 > a 
print(truthy)
```

```python
a = (int)input("Enter a number:")
truthy = not 0 < a and 100 > a 
print(truthy)
```

```python
a = (int)input("Enter a number:")
truthy = 0 < a or 100 > a 
print(truthy)
```

```python
a = (int)input("Enter a number:")
truthy = not 0 < a or not 100 > a 
print(truthy)
```

## Problem set - Selection & iteration

0. If we didn't do it as an example together in class (or you are using my notes online), create a simple number guessing game. The program needs to work as follows:

    * The computer picks a random number and stores it as a secret number
    * Ask the user to guess the number
    * If the guess is higher than the secret number, print the message "too high"
    * If the guess is lower than the secret number, print the message "too low"
    * If the guess is correct, print the message "you are correct!"
    * To use a while loop to keep the game going until the correct guess has been made
    * Bonus points: Can you keep count of the number of guesses it takes the player to get it correct?

    Note: in Python to generate a random number, you should `import random` at the top of your program, and then use an instruction such as `r = random.randint(0, 100)` to generate a random integer between 0 and 99.

1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
2. Suppose you ask the user what the temperature is. Create a program that will respond as follows:

    * If the temperature is between 20 and 27, say that it is "Just right"
    * If the temperature is below 20, say that it is "too cold"
    * If the temperature is above 27, say that it is "too hot"

3. Create a program that allows the user to input the sides of any triangle, and then return True/False to indicate if the triangle is a Pythagorean Triple or not.
4. Write a program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
5. Write a program to check a triangle is equilateral, isosceles or scalene. An equilateral triangle is a triangle in which all three sides are equal. A scalene triangle is a triangle that has three unequal sides. An isosceles triangle is a triangle with (at least) two equal sides.
6. Write a program to construct the following pattern, using a nested for loop.

```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
```

7. The fibonacci sequence is created by summing the two previous numbers together. The first 10 numbers in the sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. Use a `while()` loop to create a program that will calculate the n-th number of the sequence. For instance, if asked for the 8th number, it should provide the answer of 21.
8. Write a program to check the validity of password input by users. The rules for a valid password are:

    * At least 1 letter between [a-z] and 1 letter between [A-Z].
    * At least 1 number between [0-9].
    * At least 1 character from [$#@].
    * Minimum length 6 characters.
    * Maximum length 16 characters.

9. Write a program that will allow a user to input his name. The prompt and input data would look something like this: `Please enter your name: Peter Ustinov`. Using a for-loop and the String method, `substring()`, produce a printout of the reversal of the name. For example, the name Peter Ustinov would be: `vonitsu retep`. Ensure that the printout is in all lower-case.

## Problem set: Coding bat looping with Strings

Visit [https://codingbat.com/java](https://codingbat.com/java) and complete the Logic-1 and Logic-2 exercises

## Problem set: For loops

1. What is printed?

```java
int j=0;
for (int g = 0; g <5; g++) { 
    j++; }
System.out.println(j);
```

2. What is printed?

```java
int s=1;
for (int j = 3; j >= 0; j--) {
   s = s + j; }
System.out.println(s);
```

3. What is printed?

```java
int p=6;
int m = 20, j;
for (j = 1; j < p; j++); //Notice the semicolon on this line 
   { m = m + j * j; }
System.out.println(m);
```

4. What is printed?

```java
double a = 1.0;
for (int j = 0; j < 9; j++) {
   a*=3; }
System.out.println(j);
```

5. What is printed?

```java
for (int iMus = 0; iMus < 10; iMus++) {
   int b = 19 + iMus; }
System.out.println(b);
```

6. What is printed?

```java
double d = 100.01; int b = 0;
for (int iMus = 0; iMus < 10; iMus++) 
   b = 19 + iMus;
   d++; 
System.out.println(d);
```

7. Write a for-loop that will print the numbers 3, 6, 12, and 24

8. Write a for-loop that will print the numbers 24, 12, 6, 3

9. What is printed?

```java
int k=0;
for(int j = 0; j <= 10; j++) {
   if (j = = 5) {
      break;
   } else {
      k++; 
   }
} 
System.out.println(k);
```

10. What is the value of j for each iteration of the following loop? 

```java
int i, j;
for( i = 10; i <= 100; i = i+ 10) 
   j = i / 2;
```

11. What is the value of r after the following statements have executed? 

```java
int r, j;
for (j = 1; j < 10; j = j * 2) r = 2 * j;
```
