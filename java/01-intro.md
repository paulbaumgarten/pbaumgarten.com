# Introducing Java

Let me start with the warning: Java is not ideally suited as a "first programming language", so hopefully you have had some experience with programming in other languages before reaching this point. There is a lot of structure and complexity associated with Java that you need to get comfortable with to complete tasks that would be quite trivial in other languages such as Python.

That said, once you get the hang of the Java-way of doing things, the benefits will flow through to whatever other technology stacks you may work with in the future.  Just be prepared it will feel like qute slow-going at first.

Rather than just automatically installing an IDE to do all the work for us, it is important you understand what the IDE is doing with the core Java tools under the hood, so for the first few exercises we're going to do a lot of the work that the IDE will do for us later, manually. Bear with me, the investment of time will be worth it.

## Determining if you already have Java

To find if you have any previously existing (older?) versions of Java on your computer, look at the following locations:

* On the Mac, `/Library/Java/JavaVirtualMachines`
* On Windows `C:\Program Files\Java\jdk1.6.0_14` or similar. It may also be in your `Program Files (x86)` folder. Also on windows, from a console you can apparently use the command `where java` to locate it (if installed so as to be accessible by your system path)

You may or may not want to delete any old versions of Java. It depends on if you have other programs that use it. I can't offer guidance on that.

## Installing the Java JDK

We will use the Open JDK (Java Development Kit) rather than the proprietary Oracle JDK for this guide. Go to [https://jdk.java.net/](https://jdk.java.net/) and download the current JDK that is available and ready for use. At the time of writing it was JDK 11 and was a 174MB download.

You will download a file with a name similar to `openjdk-11.0.1_osx-x64_bin.tar` (Mac) or `openjdk-11.0.1_windows-x64_bin.zip` (Windows)

On the Mac, open a terminal:

```bash
$ cd ~/Downloads
$ tar xf openjdk-11.0.1_osx-x64_bin.tar
$ sudo mv jdk-11.jdk /Library/Java/JavaVirtualMachines/
$ java -version
$ javac -version
```

On Windows:

* Extract the zip file into a folder, e.g. `C:\Program Files\Java\` and it will create a `jdk-11` folder (where the bin folder is a direct sub-folder). You may need Administrator privileges to extract the zip file to this location.
* Set a PATH:
  * Select Control Panel and then System.
  * Click Advanced and then Environment Variables.
  * Add the location of the bin folder of the JDK installation to the PATH variable in System Variables.
  * The following is a typical value for the PATH variable: `C:\WINDOWS\system32;C:\WINDOWS;"C:\Program Files\Java\jdk-11\bin"`
* Set JAVA_HOME:
  * Under System Variables, click New.
  * Enter the variable name as JAVA_HOME.
  * Enter the variable value as the installation path of the JDK (without the bin sub-folder).
  * Click OK.
  * Click Apply Changes.
* Open a command prompt and run the following to verify:

```dos
> java -version
> javac -version
```

Windows instructions from https://stackoverflow.com/a/52531093

## Project setup

The Java-way of organising your code base is to group your functions together into "classes". The class forms the basis of individual java files of code, each class being one .java file. You then have a collection of classes that work together to form a project. You can organise related projects together into packages. Packages can then also be organised into a name based heirachy. So to summarise:

* You can have multiple "packages" of projects
* Each package can have multiple projects
* Each project can have multiple classes
* Each class can have multiple functions
* Each function represents one task/job you program Java to perform

Java uses the names of the files and folders on your disk to navigate it's way through your collections of packages, projects and classes so it is important you take care with your names. The names must be a perfect match to those you use in your code. Java is case sensititve!

## Demo: Hello world

Let's do the (in)famous "Hello world" example to walk you through what this looks like. There is an explainer for all the different elements that follows.

1. Create a folder that is going to be the base from which all your Java projects will live. On a Mac/Linux this might be "/Users/johndoe/javaprojects", on Windows it might be "C:\javaprojects".  Whereever. Pick a spot and remember it!

2. Inside your javaprojects folder, create a "src" folder and a "bin" folder. All your source code (Java programming code) will live inside "src", and all the binary files that Java creates will live inside "bin".

3. Packages, projects and classes are organised into a structure that looks like an inverted internet domain name. There is a reason for this. The intention is that it provides a mechanism for organising your classes so you can reuse them across multiple projects without names conflicting with each other. You can also import Java code that others have written, use it in your projects, and again the names should not conflict as they will use their internet domain name and you will use yours.  The following instructions are based on the school domain name "pbaumgarten.com".  If you have access to an internet domain of your own, feel free to use your own domain name details instead.

* Inside the "src" folder, create a "com" folder
* Inside the "com" folder, create an "pbaumgarten" folder
* Inside the "pbaumgarten" folder, create a "basics" folder

You should now have a folder structure that looks like this:

```
 * javaprojects
   |-- bin
   \-- src
       \-- com
           \-- pbaumgarten
               \-- basics
```

This will do for our early work. Later on, when you start using Maven or an IDE, you will need to rearrange your folders a little but the above will give you a good structure that you'll be able to drag-and-drop into the right place.

4. Using a simple text editor (I recommend VS Code but you can even use Notepad), create a file called `Exercise001.java` with the following content. Make sure you get the uppercasing/lowercasing and spacing correct!

```java
package ch.isl.basics;

public class Exercise001 {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

5. Open a terminal/console/command line interface (all terms for the same thing). Navigate to your javaprojects folder. For example:

On Mac/Linux:

```bash
$ cd /users/johndoe/javaprojects
```

On Windows:

```dos
> C:
> cd C:\javaprojects
```

6. Compile your .java file

On Mac/Linux:

```bash
javac -d bin -cp bin src/com/baumgarten/basics/Exercise001.java
```

On Windows:

```dos
javac -d bin -cp bin src\ch\isl\basics\Exercise001.java
```

(note from here on, I'll just show the Mac/Linux slash method. If you are a Windows user you'll need to remmeber to use the blackslash "\" when running javac)

7. Execute your java class

```bash
java -cp bin com.pbaumgarten.Exercise001
```

8. If all of the above was successful, you should now be able to glory in seeing the output of `Hello world!` appear in your console! Congratulations, you have just successfully written, compiled and executed a Java program!

## Explaining the Hello World program

Let's look at the Hello world program line-by-line:

```txt
1 package com.pbaumgarten.basics;
2 
3 public class Exercise001 {
4     public static void main(String[] args) {
5         System.out.println("Hello world!");
6     }
7 }
```

* Line 1 - We specify we are creating the project "ch.isl.basics". Technically the project is called "basics" and it resides in the "ch.isl" package.
* Line 3 - We declare we are creating a class called "Exercise001". This name must perfectly match the name of the ".java" file, hence why you had to save it as "Exercise001.java". Naming convention dictates a class name should begin capitalised and then be lowercase. To join multiple words together, use a capitalised letter for each new word, eg: `MyFancyClass`.
* Line 4 - Every program needs a `main()` function. This is where Java will start your program when you ask it to run. Your `main()` must be `public static void main(String[] args)`. We'll get into the specifics of what each part of this means later.
* Line 5 - This is where we actually create our output to the screen. We execute the command `System.out.println()`, supplying it the text we want printed, enclosed with the double quote characters`"Hello world!"`. The double quote characters are so Java knows where to start and stop the text it needs to take for printing.
* Line 6 - End of the main function.
* Line 7 - End of the Exercise001 class.

For the next few exercises, your code will be almost the same as above except for the content inside the main() function (line 5) which we will change depending on what we are wanting to perform.

