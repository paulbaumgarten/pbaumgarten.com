# Read & write text files

* Suggested video [Text files in Python](https://www.youtube.com/watch?v=4mX0uPQFLDU&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=29) by Socratica

Read entire file as a list, one string per line

```python
with open("countries.txt", "r") as f:   # Open file for reading
    content = f.read().splitlines()     # .read() loads entire file
    for item in content:
        print(item)
```

Writing a text file

```python
content = ['Leah', 'Obi-wan', 'Yoda', 'Rey', 'Finn', 'bb-8']
save = "\n".join(content)           # Convert list to a string, adding a new-line character after each string
with open("people.txt", "w") as f:  # Open file people.txt for writing
    f.write(save)                   # Write this string to the file
```

Notes:

* The `with` statement will close the file when you unindent
* `.splitlines()` behaves like `.split("\n")`
* Opening a file using `w` mode will overwrite an existing file
* For greater predictability, cast everything to strings before writing to files

By the way, just before we finish the section on reading/writing files, you may have wondered what the "r" or "w" in the `open()` function meant. This instructs Python how we want to access the file we request. The different modes for opening a file are as follows:

* `r` for reading
* `r+` opens for reading and writing (cannot truncate a file)
* `w` for writing (erasing it if it exist)
* `w+` for writing and reading (erasing it if it exists)
* `rb` for reading a binary file. The file pointer is placed at the beginning of the file.
* `rb+` reading or writing a binary file
* `wb+` writing a binary file
* `a+` opens for appending
* `ab+` Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
* `x` open for exclusive creation, failing if the file already exists

## OS tools

import os
file exists
file is writable
is a file, is a folder

## Problem set

> Coming soon

1. read a text file into a string
2. read a text file into a list of strings
3. write a string to a text file
4. write a list of strings to a text file
5. read a list of strings, select item you want to edit, input, update element, write back a list of strings

Write a Python program to read last n lines of a file.
Write a Python program to read first n lines of a file.
Write a Python program to count the number of lines in a text file.
Write a Python program to get the file size of a plain file.
Write a Python program to read a random line from a file.

**Challenge question**

Write a simple to-do app. Each line represents an task. The first character should be `-` if the task still needs doing, and `x` once it has been marked as complete. When the program starts, it should present the user with 3 options as follows.

```text
Welcome to simple-to-dos.
Enter the task number to mark it as complete, hit enter on an empty line to quit, or write some text to add a new task.
The tasks currently pending are:
1 Cook dinner
2 Clean bedroom
>>
```

An example of the text file follows.

```text
x Write blog post
- Cook dinner
- Clean bedroom
x Make weekly tiktok
x Subscribe to Mr B TV
```

