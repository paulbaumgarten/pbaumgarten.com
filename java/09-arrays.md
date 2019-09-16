# Arrays

So far we've talked about numbers, strings and Booleans where each variable just stores one thing at a time. 

What happens if we want to manage a shopping list? or a list of students in my class... and we want to be able to manage that entire list of things together? Java allows us to do this by creating arrays. So instead of creating variables `student1`, `student2`, `student3`, etc, we can have one variable called `students` and use that in our code.

There are two main types of arrays in Java. The classic static *array* has a size that is fixed at declaration. Once the memory space has been allocated, they can not be resized. The other type is known as *ArrayLists* and are a dynamically resizable construct available when the size of the array is not known in advance. For now, we will focus on the static array.

## Why use arrays?

It might be easiest to think of an array as the technical term for a list. It allows us to store a set of values all assigned to one variable identifier. They are very useful when we have a collection of values that are similar in nature and that will be processsed in the same manner.

For example, supposed we are keeping record of test scores obtained by a group of students. Without a list we could use something like the following:

```java
double score1 = 59.0;
double score2 = 92.0;
double score3 = 85.0;
double score4 = 61.0;
double score5 = 78.0;
```

Supposed we want to calculate the highesst, lowest and average score? That would look like...

```java
double highest = score1;        // Initially set highest to the first value
if (score2 > highest) { highest = score2; }
if (score3 > highest) { highest = score3; }
if (score4 > highest) { highest = score4; }
if (score5 > highest) { highest = score5; }
double lowest = score1;        // Initially set lowest to the first value
if (score2 < lowest) { lowest = score2; }
if (score3 < lowest) { lowest = score3; }
if (score4 < lowest) { lowest = score4; }
if (score5 < lowest) { lowest = score5; }
double average = (score1 + score2 + score3 + score4 + score5) / 5
System.out.println("The highest score was "+highest+", the lowest was "+lowest+" and the average was "+average);
```

You can see that the whole process will quickly get very tedious. There will be a lot of copy-and-pasting-and-renaming of code going on. Imagine if we needed to scale this up to 100 students for an entire year group? Unmanagable and error prone!

Enter the array!

The equivilant task using lists might look like

```java
double[] scores = {59.0, 92.0, 85.0, 61.0, 78.0};
double highest = scores[0];     // Initially set highest to the first value
double lowest = scores[0];      // Initially set lowest to the first value
double total = 0;               // Running total for calculating the average later
for (double val : scores) {     // Iterate through each `value` within `scores`
    if (val > highest) {
        highest = val;
    }
    if (val < lowest) {
        lowest = val;
    }
    total = total + value;
}
double average = total / scores.length;
System.out.println("The highest score was "+highest+", the lowest was "+lowest+" and the average was "+average);
```

Our scores array can easily contain 1000s of records and we would not have to change a single line of the calculations code! Arrays can be extremely useful!

We'll start by looking at the static array.  There are two methods to declare a static array.

## Declaring an array: method 1

```java
dint[] primes = new int[10];
primes[0] = 1;
primes[1] = 2;
primes[2] = 3;
primes[3] = 5;
primes[4] = 7;
primes[5] = 11;
primes[6] = 13;
primes[7] = 17;
primes[8] = 19;
primes[9] = 23;
```

## Declarating an array: method 2

```java
int[] primes = {1,2,3,5,7,11,13,17,19,23};
```

## Declaraing arrays of objects

> Note to my students: We will not have learnt about objects yet, so I will skip this section when teaching. It is included here so this page is a complete guide for static arrays and can refer back to it later when we want to build static arrays with objects.

What happens when the objects in your array require you to provide parameters to the constructor? You declare the array, and then instantiate each individual element. Here is an example of the technique.

```java
Student[] students = new Student[10];
students[0] = new Student("Miko", "Lausanne", "Diploma", 12, 40000);
students[1] = new Student("Tiago", "Lausanne", "Diploma", 12, 40000);
students[2] = new Student("Paolo", "Lausanne", "Diploma", 12, 40000);
students[3] = new Student("Bora", "Lausanne", "Diploma", 12, 40000);
students[4] = new Student("Ozan", "Lausanne", "Diploma", 12, 40000);
students[5] = new Student("Alessio", "Lausanne", "Diploma", 12, 40000);
students[6] = new Student("Inigo", "Lausanne", "Diploma", 12, 40000);
students[7] = new Student("Apostolos", "Lausanne", "Diploma", 12, 40000);
students[8] = new Student("Daniel", "Lausanne", "Diploma", 12, 40000);
students[9] = new Student("Misha", "Lausanne", "Diploma", 12, 40000);

for (Student individualStudent : students) {
    System.out.println(individualStudent);
}
```

## Iteration arrays

There is a special "for loop" for iterating through an array. The following two loops produce the same output.

```java
for (int item : primes) {
   System.out.println( item );
}

for (int i=0; i<primes.length; i++) {
   System.out.println( primes[i] );
}
```

## Functions and properties of arrays

Requires `import java.util.Arrays;`

```java
// Check if two arrays are filled with matching values
if ( Arrays.equals( primes, other )) {
    System.out.println("The two arrays match");
}

// Length of an array
int l = primes.length;

// Sort an array in ascending order
Arrays.sort( primes );

// Create a string listing the contents of the array
// output: [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
System.out.println( Arrays.toString( primes ));
```

## Two dimensional arrays

It is possible to create a two dimensional static array.

```java
int [][] a = {
   { 1,  2,  3,  4,  5 },
   { 11, 12, 13, 14, 15 },
   { 21, 22, 23, 24, 25 }
};
System.out.println( a[i][j] );
```

Two dimensional array where values are not pre-known

```java
int [][] a = new int[3][5];
```

To iterate over the 2D array

```java
for (int[] row : a ) {
    for (int cell : row) {
        System.out.println( cell );
    }
}
```

## Problem set: Arrays

For some introductory level questions, I recommend solving the problem sets on coding bat:

* [Array-1 coding.bat problems (no loops)](https://codingbat.com/java/Array-1)
* [Array-2 coding.bat problems (require 1 loop)](https://codingbat.com/java/Array-2)
* [Array-3 coding.bat problems (require 2 loops & complex logic)](https://codingbat.com/java/Array-3)

Be warned, a number of the questions in the main problem set are quite challenging for new programmers. Do not worry if you feel some of them are beyond you if you are at the beginning stags of learning to program. Revisit the questions you can't do after you have been programming consistently for about 12 months.

Note: Use Arrays or ArrayLists as you feel best fits the problem. Do ensure you practice using a mix of both.

1. Write a program to sum all the items in an array.
2. Write a program to get the largest number from an array.
3. Write a program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
4. Write a program to find duplicates from an array and print a message that it exists as a duplicate.
5. Write a function that takes two array and returns `true`` if they have at least one common member.
6. Write a program to print the contents of an array of integers, ignoring any numbers in it.
7. Given two arrays, write a program to print the items that are not in both arrays.
8. Write a program to select an item randomly from an array. Once drawn, you should shuffle all the remaining items in the array down and set the last value to `null` and deduct a value from a pointer keeping track of the number of populated items so that it can't be re-drawn again. (just like a deck of cards scenario)

    For example, given an array `{4, 7, 10, 13, 5}` and `itemCount = 5`; if you were to randomly draw position `1`, you print the value `7`, and then update the array to the values `{4, 10, 13, 5, null}` and set `itemCount = 4`.

    For question 8, you may like to copy and paste the following as an array to use:

    ```java
    String[] deck = {
        "A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️",
        "A♥️", "2♠️️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
        "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
        "A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️",
    };
    ```

    (ps - remember the java.lang.Math library provides a random number function)
