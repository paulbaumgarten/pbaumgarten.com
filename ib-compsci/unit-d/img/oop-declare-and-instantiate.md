# OOP: Declaring and instantiating in Java

When doing this what is going on? Why is *ClassName* required twice?

```java
ClassName instancename = ClassName();
```

**Explaination**

On the left hand:

```java
ClassName instancename
```

The ClassName is declaring type (= class) of variable instancename.

On the right hand:

```java
new ClassName();
```

The ClassName() is invoking a (constructor) method named ClassName().

So, you are doing two things at once.

```java
ClassName instancename;         // declaring type
instancename = new ClassName(); // invoking method
```

Your example:

```java
ClassName instancename = new ClassName();
```

is just shortened style of the two instructions.

via [StackOverflow](https://stackoverflow.com/questions/33173063/why-do-we-have-to-type-the-class-name-twice-when-instantiating-a-new-object-in-j)
