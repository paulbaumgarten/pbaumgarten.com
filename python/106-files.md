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
save = "\n".join(content)           # Convert list to a string
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

## Problem set

This problem draws on all the programming skills you have learnt so far to create a text based hang-person game. To build this exercise, you will need to successfully complete the following:

* Load the words text file into a list (array)
* Use the random number generator to randomly select one item from the list as the secret word
* Reveal the secret word while hiding the letters not yet guessed
* Use a loop to keep asking the player to guess a new letter
* If a guessed letter is not in the secret word, increase their wrong guesses count and draw the new hangman.
* If a guessed letter is in the word, add it to your list of correct guesses.
