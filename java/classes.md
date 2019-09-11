# Java: Classes

> This assumes an understanding of Object Orientated Programming. It is intended as a quick refresher to the Java implementation of OOP, nothing more. Check my separate [IB Computer Science teaching notes on Object Orientated Programming](https://github.com/paulbaumgarten/ib-compsci-notes/tree/master/unit-d) for a more thorough grounding into the theory involved and its use in Java.

## An example Java class

```java
package com.pbaumgarten.basics;

public class DemoClass{
    private int data;           // Instance variable - note the 'private' access modifier

    DemoClass() {             // Constructor - must be same name as the class
        data = 0;               // Initialise our instance variables
    }

    public void setData( int i ) {
        data = i;               // Set the instance variable
    }

    public void setDataAlternative( int data ) {
        /* Because the parameter variable is the same name as the instance variable, we use the "this" keyword to specify when we want to access the instance variable. */
        this.data = data;
    }

    public void doubleData() {
        data = 2 * data;
    }

    public int getData() {
        return( data );
    }

    public static void main( String args[] ) {
        DemoClass obj = new DemoClass();        // Instantiate the object
        obj.setData( 10 );                      // Call the .setData() method
        obj.doubleData();                       // Call the .doubleData() method
        int val = obj.getData();                // Call the .getData() method
        System.out.println( val );
    }
}
```

Before moving on, ensure you understand the significance of:

* Instance variables. These are the variables that belong to each object instance of the class. In the above example, `data` is an instance variable.
* Constructors. This is the code executed when the object is instantiated. It is always public, and is defined by being a function of the same name as the class itself. In the above example, the `ExerciseA01()` function that initialises data to zero is the constructor. Constructors may accept parameters, and may be overloaded (see below).
* Instantiation. This is the process of creating an object based on a class. In our example, the `obj` object is being instantiated in the first line of the `main()`.

---

## Inheritance

The magic happens with the use key word **extends**

```java
public class Automobile {
    String registration;
    String owner;

    Automobile(String registration, String owner){
        this.registration = registration;
        this.owner = owner;
        System.out.println("Vehicle "+registration+" registered to "+owner);

    }
    String getOwner() {
        return owner;
    }
}

public class Motorcycle extends Automobile {
    String make;
    String model;
    String serialnumber;
    int enginesize;

    Motorcycle(String registration, String owner, String make, String model){
        super(registration, owner);
        this.make = make;
        this.model = model;
    }

    void printRegistration() {
        System.out.println("Motorcycle: "+registration);
        System.out.println("Owner: "+owner);
        System.out.println("Make: "+make);
        System.out.println("Model: "+model);
    }

    public static void main() {
        Motorcycle m = new Motorcycle("VD-12345","John Doe","Harley","Breakout");
        m.printRegistration();
        System.out.println("The owner is: " + m.getOwner() );
    }
}
```

---

## Encapsulation

Encapsulation binds the data with the code that manipulates it; and keep the data and the code safe from external interference.

One key mechanism for enforcing encapsulation is the use of access modifiers. The access modifiers in Java are:

* public – visible to the world
* protected – visible to the package and all sub classes
* default (no access modifier provided) - visible to the package
* private – visible to the class only

Example:

```java
public class A {
   private int x;

   public void setX( int x ) {
      this.x = x;
   }

   public int getX() {
      return x;
   }
}

public class B {
   public static void main() {
      A a = new A();
      a.setX( 13 );
      System.out.println( a.getX() );
      a.x = 14;      // this will cause an error as x is private
      System.out.println( a.getX() );
   }
}
```

---

## Polymorphism: Overloading

Multiple functions with the same name but different parameter inputs. Java will determine which function to run based on which matches the set of parameters you provide.

```java
void driveForward() {           // First occurance of driveForward(), no parameter expected
    speed = 60;
}

void driveForward(int s) {      // Overloading driveForward() with one that accepts 1 parameter
    speed = s;
}
```

## Polymorphism: Overriding

When a function in a child class has the same name as a function in the parent class, the child class' version will take precedence.

Example:

```java
public class Person {
    String name;
    Person(String name) {
        this.name = name;
    }
    String getName() {
        return this.name;
    }
}

public class Royalty extends Person {
    Royalty(String name) {
        super(name);
    }
    String getName() {   // Overriding the .getName() method in Person
        return "Your Royal Highness "+name;
    }
}

public class Demo {
    public static void main() {
        Person commoner = new Person("John");
        System.out.println( commoner.getName() );
        Royalty queen = new Royalty("Elizabeth");
        System.out.println( queen.getName() );   // Will run the overriden getName() method
   }
}
```
