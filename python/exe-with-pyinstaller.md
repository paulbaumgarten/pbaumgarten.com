
# Creating a distributable EXE

## Installing PyInstaller

From console:

* `pip install pyinstaller` or
* `pip install --user pyinstaller`

From Pycharms (Windows) - part 1  

* File / settings / project / project interpreter
* Install package (the green 'plus' icon)
* Package name is 'PyInstaller'
* Remember to tick the 'Install to user's site packages directory' option
* Write down the location of the site packages directory - you will need it later
* Click "Install package"
* Close once complete

From Pycharms (Windows) - part 2  

* File / settings / tools / external tools
* Add (green 'plus' icon)
* Name: `PyInstaller` or other meaningful name
* Description: `Make an EXE file`
* Program: `C:\Users\YOURUSERNAME\AppData\Roaming\Python\Python36\Scripts\pyinstaller.exe` ... Note: This is where you need to know your site packages directory. Type that part in first, then click the three dot icon on the right `...` and navigate the folders until you reach the `PyInstaller.exe` file.
* Parameters: `--clean --onefile $FilePath$ $Prompt$`
* Working directory: `$ProjectFileDir$`
* Click OK

## Modify your code

The main difficulty with the manner that pyInstaller works, is the way it handles "extra" files you want to use (such as images, music/sounds etc). When run, the EXE file will put these in a randomly created temporary folder. You need to modify your code so it knows where to find these files. Add the following function to your code:

```python
def get_true_filename(filename):
    try:
        # Hack for pyInstaller. Refer https://stackoverflow.com/a/13790741
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, filename)
```

Now, where ever you are loading those images, sounds etc in your project, modify the code as follows:

From:  

```python
SPRITE = pygame.image.load("my_sprite.png")
```

To:  

```python
SPRITE = pygame.image.load(get_true_filename("my_sprite.png"))
```

## Create the EXE file

Using pyCharm:

* Open the python file that your project opens with
* Right click / External tools / PyInstaller
* At the "Enter paramters" box type `--add-data *.wav;. --add-data *.png;. --add-data *.jpg;.` (etc ... for all the types of files you need added)
* Note the semi colon and the dot after each type of file in the above line.

Using console:

`pyinstaller --clean -–onefile myscript.py --add-data *.wav;. --add-data *.png;. --add-data *.jpg;.`

* Note the semi colon and the dot after each type of file in the above line.

## Notes

* The output of PyInstaller is specific to the active operating system and the active version of Python. 
* On Mac/Linux the `--add data` format uses a colon instead of semi-colon.
* The `--add-data` can take folder names, and copy the contents to relative folder names. eg: `--add-data media/*;media`
