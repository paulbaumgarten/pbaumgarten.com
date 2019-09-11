# Command line reference

The following is a summary of useful console commands. All commands should be executed from your `javaprojects` folder.

## Compile Java

* To compile a .java class into a .class file

```bash
javac -d bin src/ch/isl/basics/Exercise001.java
```

* To compile a .java class into a .class file where you need to specify a classpath for imports as well

```bash
javac -d bin -cp bin src/ch/isl/basics/Exercise001.java
```

* To compile where you need to import a .jar file as well, or to list multiple class paths

(On Windows, replace the colon `:` with the semi-colon `;`)

```bash
javac -d bin -cp bin:project.jar src/ch/isl/basics/Exercise001.java
```

* To compile where you need to import multiple .jar files as well, or to list multiple class paths

Place all `.jar` files into a `lib` folder and use the wildcard like so...

(On Windows, replace the colon `:` with the semi-colon `;`)

```bash
javac -d bin -cp bin:lib/* src/ch/isl/basics/Exercise001.java
```

* To (re)compile all .java class files in all your sub-folders (handy shortcut!)

On Mac/Linux:

```bash
cd ~/javaprojects
find src -name "*.java" > sources.txt
javac -d bin @sources.txt
```

On Windows:

```dos
cd C:\javaprojects
dir /s /B *.java > sources.txt
javac -d bin @sources.txt
```

## Executing Java

To execute the main function within a .class file

```bash
java -cp bin ch.isl.basics.Exercise001
```

## JAR files

There are two types of jar files (Java ARchive files): Executable and non-executable. The non-executable type lack the presence of a `main()` function and are used for creating libraries of classes intended for importing into other projects. The executable type must contain (and specify) a `main()` function so it can be executed.

* To create a non-executable jar of the contents of `bin`:

```bash
jar cvf myproject.jar -C bin .
```

* To create an executable jar of the contents of `bin`, specifing the class path to where `main()` function resides:

```bash
jar cfe myproject.jar com.example.Project -C bin .
```

* To execute the main function within a .jar file use either of the following

```bash
java -cp myproject.jar com.example.Project
java -jar myproject.jar
```

