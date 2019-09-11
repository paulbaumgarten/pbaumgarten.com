# Java: Files & folders

Be aware, when you start searching for anything to deal with file handling in Java, you will quickly encounter a lot of different ways of doing it. Which method is "most" correct? Which method do you use when? To be honest, at this point in your porgramming journey, don't worry too much about speed or memory efficiency issues, find a method that seems "logical" to you and stick with it.

To demonstrate, these are the different classes available for file reading in Java:

* java.io.FileReader.read() - reads in one character at a time, without any buffering. It’s meant for reading text files.
* java.io.BufferedReader.readLine() - reads an entire line at a time,
* java.io.FileInputStream.read() - reads in one byte at a time, without any buffering. While it’s meant for reading binary files such as images or audio files, it can still be used to read text file.
* java.io.BufferedInputStream.read() - reads a set of bytes all at once into an internal byte array buffer
* java.nio.file.Files.readAllBytes() - The Files class is part of the new Java I/O classes introduced in jdk1.7. It only has static utility methods for working with files and directories.
* java.nio.file.Files.readAllLines() - The Files class is part of the new Java I/O classes introduced in jdk1.7. It only has static utility methods for working with files and directories.
* java.nio.file.Files.lines() - The Files class is part of the new Java I/O classes introduced in jdk1.7. It only has static utility methods for working with files and directories.
* java.util.Scanner.nextLine() - can be used to read from files or from the console (user input)
* org.apache.commons.io.FileUtils.readLines() – Apache Commons
* com.google.common.io.Files.readLines() – Google Guava

The following is a useful reference that outlines each of the above techniques:

* [Ultimate Guide for Reading Files in Java](https://funnelgarden.com/java_read_file/)

## Sample recipes for files

Read a text file into an ArrayList (one entry per line)

```java
package ch.isl.helpers;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class Files {
    public static ArrayList<String> readFile(String filename) {
        ArrayList<String> content = new ArrayList<String>();
        try {
            File f = new File(filename);
            Scanner reader = new Scanner(f);
            while (reader.hasNextLine()) {
                content.add(reader.nextLine());
            }
            reader.close();
        } catch(Exception e) {
            // This shouldn't be empty, what happens if the filename is misspelt, file has been deleted, permissions problems, etc?
        }
        return content;
    }

    public static void main(String[] args) {
        String fname = "/Users/pbaumgarten/ISL/projects/java/sources.txt";
        ArrayList<String> data = readFile(fname);
        System.out.println(data);
    }
}
```

Write ArrayList of strings to a text file

```java
package ch.isl.helpers;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Files {
    public static boolean saveFile(String filename, ArrayList<String> content) {
        try {
            FileWriter fw = new FileWriter(filename);
            PrintWriter output = new PrintWriter(fw);
            for (String line: content) {
                output.println( line );
            }
            output.close();
            fw.close();
            return true;
        } catch(Exception e) {
            return false;   // error occurred in saving file
        }
    }

    public static void main(String[] args) {
        // Create the dummy data to save to our file
        ArrayList<String> data = new ArrayList<String>();
        data.add("first");
        data.add("second");
        data.add("third");
        data.add("forth");
        data.add("fifth");
        // Save to file
        String fname = "/Users/pbaumgarten/ISL/projects/java/test-file-save.txt";
        boolean ok = saveFile(fname, data);
    }
}
```

## Folder walk

```java
// From: https://stackoverflow.com/a/2056326
package ch.isl.helpers;
import java.io.File;

public class Files {

    public static void walk( String path ) {
        File root = new File( path );
        File[] list = root.listFiles();
        if (list == null) return;
        for ( File f : list ) {
            if ( f.isDirectory() ) {
                System.out.println( "Dir:" + f.getAbsoluteFile() );
                walk( f.getAbsolutePath() );
            }
            else {
                System.out.println( "File:" + f.getAbsoluteFile() );
            }
        }
    }

    public static void main(String[] args) {
        walk("c:\\" );
    }
}
```

Other ways of implementing this are discussed at:

* https://docs.oracle.com/javase/tutorial/essential/io/walk.html
* https://rosettacode.org/wiki/Walk_a_directory/Recursively#Java

