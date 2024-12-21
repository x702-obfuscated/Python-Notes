# `Python File Handling`

*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

<br>

___

<br>

Covered in this file:
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()


<br>

___

<br>

# `File Extensions`
A `file extension` is a suffix that is added to the end of a filename to indicate the type of file. 
* A file extension is typically separated from the rest of the filename by a period (.)

<br>

*In Windows file extensions are required, but often hidden by the file explorer.*

*In GNU/Linux systems file extensions are not required, but are often used by convention to help users identify file contents.*

<br>

Python Files use the extension `.py` for source code.
```
main.py
```

<br>

`.pyc` is used for compiled python bytecode files
```
main.pyc
```

<br>

[Back to Top](#python-file-handling)

___

<br>



# `File Paths`
A `file path` is a string of characters that identifies the location of a file on a computer storage device. 

<br>

File paths can be `absolute` or `relative`.

<br>

An `absolute file path` specifies the complete location (address) of a file, starting from the root directory. 

<br>

The `root directory` is the topmost directory in a file system hierarchy. It serves as the starting point or base from which all other directories and files branch out. `It is the folder that contains all other folders.` 

<br>

* `Unix/Linux/MacOS`: The root directory is represented by a single forward slash `/`.
* `Windows`: The root directory is specific to each drive and represented by a backslash `\` following the drive letter.

<br>

GNU-Linux
```
/home/John/Documents/file.txt
```
Windows
```
C:\Users\John\Documents\file.txt
```

<br>

A `relative file path` specifies the location of a file relative to the current working directory (current location). 

* `.` is a reference to the current working directory
s
* `..` is a reference to the parent directory of the current working directory

<br>


For more on file extensions see:  
[LearningWithMerritt/Classroom-Notes/4-Operating-Systems/2-General/file-extensions.md](https://github.com/LearningWithMerritt/Classroom-Notes/blob/main/4-Operating-Systems/2-General/file-extensions.md)

For more on files on the Windows OS see:  
[LearningWithMerritt/Classroom-Notes/4-Operating-Systems/0-Windows/windows-filesystem.md](https://github.com/LearningWithMerritt/Classroom-Notes/blob/main/4-Operating-Systems/0-Windows/windows-filesystem.md)

For more on files on the GNU-Linux OS see:  
[LearningWithMerritt/Classroom-Notes/4-Operating-Systems/1-GNU-Linux/linux-filesystem.md](https://github.com/LearningWithMerritt/Classroom-Notes/blob/main/4-Operating-Systems/1-GNU-Linux/linux-filesystem.md)


<br>

[Back to Top](#python-file-handling)

___

<br>


# `Working with the Filesystem`
See 7-Advanced/Importing-Code/2-Modules/os_module.md


# `Opening and Closing Files`
Text mode
Binary mode

buffering
encoding
errors
newline
closefd
opener


method
.close()

```python
#absolute path
#relative path

#open(path,mode)
file = open("file.txt",'r') #read
file.read() #reads entire content
file.readlines() #reads and returns all lines as a list
file.close()
```
```python
def open(file, mode='r', buffering=-1, encoding=None, 
         errors=None, newline=None, closefd=True, opener=None):
    """
    Open file and return a corresponding file object.

    Parameters:
    - file: The file path or file descriptor to open.
    - mode: A string indicating how the file is to be opened (default is 'r').
      Common modes:
      - 'r': Read (default)
      - 'w': Write (overwrites if file exists)
      - 'x': Exclusive creation
      - 'a': Append
      - 'b': Binary mode
      - 't': Text mode (default)
      - '+': Read and write
    - buffering: Controls buffering. -1 for default buffering.
    - encoding: Name of the encoding (used in text mode).
    - errors: Error handling scheme for encoding/decoding.
    - newline: Controls how newlines are handled (text mode only).
    - closefd: Must be True if a file name is given.
    - opener: A custom opener.

    Returns:
    A file object whose type depends on the mode.

    Raises:
    - FileNotFoundError: If the file cannot be found (when in 'r' mode).
    - ValueError: If the mode is invalid.
    - OSError: For other errors like permission issues.
    """

    # Open a file in read mode (default)
file = open('example.txt', 'r')

# Open a file in write mode (overwrites if exists)
file = open('example.txt', 'w')

# Open a file in binary mode for reading
file = open('example.txt', 'rb')

# Open a file with custom encoding
file = open('example.txt', 'r', encoding='utf-8')

```
Always close files after use, or better, use the with statement.
Handle file exceptions using try...except blocks.
Be cautious when using 'w' mode as it overwrites existing files.



<br>

[Back to Top](#python-file-handling)

___

<br>

# `Context Management`
__enter__()
__exit__()
with

```python
#Using Context Managers (with statment)
#automatically closes files
with open("file.txt","r") as file:
    print( file.read() )
```


# `Creating Files`
exclusive creation


# `Reading From Files`
read

methods
read()
readline()
readlines()


read(size=-1)	Reads the specified number of bytes (or all bytes if size is not provided).
readline(size=-1)	Reads a single line from the file. Optionally, limit the length using size.
readlines(sizehint=-1)	Reads all lines of the file into a list. Optionally, provide sizehint for approximate size.
write(string)	Writes the given string to the file.
writelines(lines)	Writes a list of strings to the file.
close()	Closes the file. Ensures no more operations can be performed on the file.

# `Writing To Files`
write   
appendqeqe

methods
write()
writelines()

```python
file = open("file.txt",'w') #write
file.write("New Content ") #Overwrites file with new content
file.writelines(["line1","line2","line3"]) #Overwrites file lines using a list of string
file.close()

open("file.txt", 'a') #append
file.write("New content added to the end of the file")
file.close()
#close files after working with them
```

# `Read and Write`
+

# `File Pointers`
Method	Description
seek(offset, whence=0)	Moves the file pointer to a specific position. offset is the position, and whence determines the reference point:
0 (default): Beginning of file
1: Current position
2: End of file
tell()	Returns the current position of the file pointer.

# `File Buffering and Flushing`
flush()
fileno()
isatty()

# `Error Handling`
try-except

# `Checking File Status`
Method	Description
closed	Returns True if the file is closed, otherwise False.
mode	Returns the mode in which the file was opened (e.g., 'r', 'w', 'rb').
name	Returns the name of the file.
encoding	Returns the encoding of the file (text files only).
errors	Returns the error-handling scheme used when encoding/decoding (e.g., 'strict', 'ignore').
newlines	Returns the newline character(s) found in the file (None, '\n', '\r', or '\r\n').

<br>

[Back to Top](#python-file-handling)

___

<br>



