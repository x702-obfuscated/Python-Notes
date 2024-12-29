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

## `Common File Extensions`

| **Extension**    | **Description**                            |
|-------------------|-------------------------------------------|
| `.doc` / `.docx`  | Microsoft Word Document                   |
| `.pdf`            | Portable Document Format                 |
| `.txt`            | Plain Text File                          |
| `.rtf`            | Rich Text Format                         |
| `.odt`            | OpenDocument Text Document               |
| `.xls` / `.xlsx`  | Microsoft Excel Spreadsheet              |
| `.csv`            | Comma-Separated Values                   |
| `.ppt` / `.pptx`  | Microsoft PowerPoint Presentation        |
| `.jpg` / `.jpeg`  | JPEG Image                               |
| `.png`            | Portable Network Graphic                 |
| `.gif`            | Graphics Interchange Format              |
| `.bmp`            | Bitmap Image                             |
| `.svg`            | Scalable Vector Graphics                 |
| `.tiff`           | Tagged Image File Format                 |
| `.webp`           | WebP Image                               |
| `.mp3`            | MPEG Audio Layer III                     |
| `.wav`            | Waveform Audio File Format               |
| `.flac`           | Free Lossless Audio Codec                |
| `.aac`            | Advanced Audio Coding                    |
| `.ogg`            | Ogg Vorbis Audio File                    |
| `.mp4`            | MPEG-4 Video                             |
| `.avi`            | Audio Video Interleave                   |
| `.mkv`            | Matroska Video                           |
| `.mov`            | QuickTime Movie                          |
| `.wmv`            | Windows Media Video                      |
| `.flv`            | Flash Video                              |
| `.zip`            | ZIP Archive                              |
| `.rar`            | RAR Archive                              |
| `.7z`             | 7-Zip Archive                            |
| `.tar`            | TAR Archive                              |
| `.gz`             | Gzip Compressed File                     |
| `.bz2`            | Bzip2 Compressed File                    |
| `.exe`            | Windows Executable                       |
| `.bat`            | Batch File                               |
| `.sh`             | Shell Script                             |
| `.jar`            | Java Archive                             |
| `.app`            | macOS Application                        |
| `.py`             | Python Script                            |
| `.java`           | Java Source File                         |
| `.js`             | JavaScript File                          |
| `.html`           | Hypertext Markup Language                |
| `.css`            | Cascading Style Sheets                   |
| `.json`           | JavaScript Object Notation               |
| `.xml`            | Extensible Markup Language               |
| `.yml` / `.yaml`  | YAML File                                |
| `.dll`            | Dynamic Link Library                     |
| `.sys`            | Windows System File                      |
| `.log`            | Log File                                 |
| `.ini`            | Initialization File                      |
| `.iso`            | Disc Image File                          |
| `.apk`            | Android Package File                     |
| `.deb`            | Debian Package                           |
| `.pkg`            | macOS Installer Package                  |
| `.torrent`        | Torrent File                             |


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
* `..` is a reference to the parent directory of the current working directory

```
./file.txt
```
```
../file.txt
```

<br>

## `A note on Windows Paths`
Since Windows uses `\` as a path delimiter there is a conflict witht the `\` character being used as a escape character. 

Here are a two ways to handle this issue in Python:

<br>

Use `\\` to escape the `\` character
```python
windows_path = "C:\\Users\\USERNAME\\Documents\\file.txt"
```

<br>

Use a Raw String with `r`  
*`Note that this solution may conflict with the use of escape characters.`*
```python
windows_path = r"C:\Users\USERNAME\Documents\file.txt"
```

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
See the built-in `os` module for working with the filesystem:  
[LearningWithMerritt/Python-Notes/7-Advanced/Importing-Code/1-Modules/os.md](../Importing-Code/1-Modules/os.md)


<br>

[Back to Top](#python-file-handling)

___

<br>



# `Opening and Closing Files`
Working with files is an essential skill for programmers because it allows for reading, writing, and managing persistant data from on execution to the next. 

In Python, opening files is accomplished using the `open()` function. 
* `open()` opens a file, and returns a file object

*`It is best practice to use a context manager when working with files in python`*  
See >>> [Context Management](#context-management)

The actual `open()` function is defined in C, however below is a representation of its header if it was written in Python. 
```python
def open(
  file, mode='r', buffering=-1, 
  encoding=None, errors=None, newline=None, 
  closefd=True, opener=None
  ):
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
```

Syntax:
```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
```python
open("/path/to/file.txt") 
```
```python
open("/path/to/file.txt", "r")
```

<br>

[Back to Top](#python-file-handling)

___

<br>

## `mode`

| **Mode**  | **Description**| **Example**|
|---|--|---|
| `r` | Open for reading (default). `The file must exist.`| `open('file.txt', 'r')`|
| `w` | Open for writing. `Creates a new file or truncates an existing file.` | `open('file.txt', 'w')`|
| `x` | Open for exclusive creation. `Fails if the file already exists`. | `open('file.txt', 'x')`|
| `a` | Open for appending ie. writes to the end of the file. `Creates a new file if it does not exist.`| `open('file.txt', 'a')`|
| `b` | Open in binary mode. Used in combination with other modes. | `open('file.txt', 'rb')` |
| `t` | Open in text mode (default). Used for reading/writing text files.| `open('file.txt', 'rt')` |
| `r+`| Open for reading and writing. The file must exist.| `open('file.txt', 'r+')` |
| `w+`| Open for reading and writing. Creates a new file or truncates an existing file. | `open('file.txt', 'w+')` |
| `a+`| Open for reading and appending. Creates a new file if it does not exist. | `open('file.txt', 'a+')` |

<br>

[Back to Top](#python-file-handling)

___

<br>

## `Text Mode vs Binary Mode` 

| **Feature** | **Text Mode (`'t'`)**| **Binary Mode (`'b'`)** |
|--|--|---|
| **Data Type** | Characters (text)| Raw bytes (no conversion) |
| **Encoding**| Automatically encoded (default or specified) ("utf-8","ascii",etc)| No encoding (raw binary data) |
| **Newline Handling**| Newlines translated (`\n` to `\r\n` on Windows) | No newline translation (raw `\n` or `\r\n`) |
| **Usage** | Text files (e.g., `.txt`, `.csv`, `.json`) | Binary files (e.g., `.jpg`, `.png`, `.exe`) |

<br>

``When to Use Each:``
- **Text Mode**: When dealing with text files where encoding and newline handling are important.
- **Binary Mode**: When working with non-text files where byte-level precision is necessary, such as images, videos, and executable files.

<br>

[Back to Top](#python-file-handling)

___

<br>

## `Encoding and Error Handling`
`encoding` specifies the character encoding used when reading from or writing to a file.

```python
with open('example.txt', 'w', encoding='ascii', errors='replace') as f:
    f.write("Hello, world! Привет мир!")
```

*In this example, the non-ASCII characters "Привет мир!" would be replaced with '�' because they cannot be represented in ASCII.*



When working in binary mode and converting from text to binary or vice versa the `.encode()` and `.decode()` string methods are useful. 


`.decode()` converts binary to its text representation
Syntax:
```
string.decode(encoding="utf-8",errors="strict") 
```

```python
with open("file.txt", "rb") as file:
  contents = file.read()
  print(contents.decode("utf-8"))
```

<br>

`.encode(encoding)` converts a string into its binary representation
Syntax:
```
string.encode(encoding="utf-8",errors="strict")
```
```python
text = "Hello World!"

with open("file.txt", "wb") as file:
    file.write(text.encode("utf-8"))
```

<br>

| **Parameter** | **Description**| **Common Values** |
|--|--|--|
| **encoding** | The encoding format to use when converting between bytes and text. The default is `'utf-8'`. | `'utf-8'`, `'ascii'`, `'latin-1'`, `'utf-16'`, `'utf-32'`, etc. |
| **errors** | Specifies how to handle decoding errors. | `'strict'`, `'ignore'`, `'replace'`|

<br>

### `Common Encoding Formats Supported in Python:`
| **Encoding** | **Description**|
|--|---|
| `'utf-8'`| Unicode Transformation Format 8-bit. The most commonly used encoding for web and file content. |
| `'ascii'`| American Standard Code for Information Interchange. Only supports characters in the range 0-127. |
| `'latin-1'`| Also known as ISO-8859-1, commonly used in Western European languages. |
| `'utf-16'` | UTF encoding using 16 bits per character. Supports a wider range of characters compared to UTF-8. |
| `'utf-32'` | UTF encoding using 32 bits per character. Supports a wide range of characters. |
| `'cp1252'` | Windows-1252, a common encoding for Windows-based systems in Western Europe and the Americas. |
| `'big5'` | Traditional Chinese encoding, used primarily in Taiwan and Hong Kong. |

<br>

### `Error Handling Options:`
| **Error Handling** | **Description** |
|--|--|
| `'strict'` | Default behavior. Raises a `UnicodeDecodeError` if decoding fails. |
| `'ignore'` | Ignores any bytes that cannot be decoded, skipping over them. |
| `'replace'`| Replaces undecodable bytes with a placeholder character (usually `'�'`). |

<br>

[Back to Top](#python-file-handling)

___

<br>

## `Buffering`
`Buffering` refers to the process of storing data in a temporary memory area (the buffer) before reading or writing it to the file, which can improve I/O performance by reducing the number of system calls.

<br>


| **Buffering Value** | **Description**| **Use Case**|
|--|------|----------|
| `0` | No buffering. Data is read or written immediately without being stored in a buffer. | Used for binary files or when you need immediate I/O operations.|
| `1` | Line buffering. Data is buffered until a newline character (`\n`) is encountered. | Commonly used for text files, especially when processing line-by-line. |
| `n`(>1) | Custom buffer size (integer greater than 1). The data is buffered in chunks of the specified size in bytes. | Optimizes I/O operations for large files or frequent read/write operations. |
| `-1` (default)| Default buffering behavior, which is usually automatic buffering based on the system's default. | Most common case, with automatic optimizations based on the system. |

<br>

```python
with open('example.txt', 'w', buffering=8192) as f:
    f.write('This file is written with a buffer size of 8192 bytes.')
```

<br>

[Back to Top](#python-file-handling)

___

<br>

## `Newline`
`newline` controls how newline characters (\n, \r, \r\n) are translated when reading or writing a file.

<br>


| **Option** | **Description** | **Use Case** |
|------------|-----------------|--------------|
| `None`     | Default behavior. Platform-specific newline handling (e.g., `\r\n` on Windows, `\n` on Unix-based systems). | Most common case, handles newlines according to the operating system’s default behavior. |
| `''`       | No newline translation. Reads and writes the newline characters as-is. | Useful when you want to preserve the exact newline characters in the file, without any modification. |
| `\n`       | Forces Unix-style newline (`\n`). Converts all newlines to `\n`. | Useful for ensuring consistency when working with files on different platforms or with specific formats. |
| `\r\n`     | Forces Windows-style newline (`\r\n`). Converts all newlines to `\r\n`. | Ensures compatibility with Windows-based applications or when handling files with Windows-style newlines. |
| `\r`       | Forces Mac-style newline (`\r`). Converts all newlines to `\r`. | For legacy systems that use old Mac-style newlines (used by Mac OS 9 and earlier). |


<br>

[Back to Top](#python-file-handling)

___

<br>

## `closefd`
`closefd` determines whether the underlying file descriptor should be closed when the file object is closed.
* closefd can be True or False
* default is True (close the file descriptor)
* False leaves the descriptor open

<br>

A `file descriptor` is a low-level integer identifier used by an operating system to represent an open file or input/output (I/O) resource. It acts as a reference that allows programs to interact with files or other I/O resources (such as pipes, sockets, and devices) in a system.

<br>

`.fileno()` returns the file descriptor of a file object
```python
with open('example.txt', 'w') as file:
    print(file.fileno())  # Print the file descriptor (an integer)
```

<br>

[Back to Top](#python-file-handling)

___

<br>


## `opener`
`opener` is used to define a custom function for opening the file.
* this function is called when the file is opened

<br>

[Back to Top](#python-file-handling)

___

<br>

## `Closing Files`

`FILES MUST BE CLOSED`

*Always close files after use, or better, use a context manager (the with statement.)*

<br>

*Closing files is necessary because it ensures that all data written to the file is properly saved and that system resources used to manage the file are released. When a file is open, the operating system allocates resources such as memory buffers and file descriptors. If the file is not closed, these resources remain in use, which can lead to memory leaks or file access issues. Additionally, in some cases, data written to a file may remain in a temporary buffer until the file is closed, meaning failing to close it could result in incomplete or lost data. Properly closing files also helps prevent file corruption and allows other programs or processes to access the file without conflicts.*

<br>

File objects are closed using the `.close()` method.

*Context Managers handle the closing of files and are considered best practice in most cases*

<br>

Syntax:
```
file.close()
```
```python
file.close()
```

<br>

[Back to Top](#python-file-handling)

___

<br>

# `Context Management`
Context management refers to the management of resources efficiently and automatically, such as opening and closing files. 

`with` is used to define the context
* This is considered best practice when handling files, because it ensures proper closing of the file.

Syntax:
```
with expression as variable:
  ...
```
```python
with open("file.txt", "r") as file:
  print(file.read())
```



<br>


`__enter__()` and `__exit__()` are methods implemented within a class that define the behaviour of an object when entering and exiting a `with` block.

<br>

```python
def __enter__(self):
  '''Called when entering the context of a with block'''
  ...
```
```python
def __exit__(self, exc_type, exc_value, traceback):
  '''Called when exiting the context of a with block'''
  ...
```

<br>

```python
with open("file.txt", "r") as file: # __enter__() is called here
    file.read()
# __exit__() is called here
```

`__exit__() handles proper cleanup after the use of the file to ensure resoures are properly released, etc. `

<br>

[Back to Top](#python-file-handling)

___

<br>


# `Creating Files`
See the built-in `os` module for more on working with the filesystem:  
[LearningWithMerritt/Python-Notes/7-Advanced/Importing-Code/1-Modules/os.md](../Importing-Code/1-Modules/os.md)

<br>

Files can and will be created if they do not already exist when using the `open()`function in certain modes.

### `open() modes that can create a file`

| Mode  | Creates File? (If it doesn't exist) | Overwrites Existing?  |Example|
|-------|-------------------------------|------------------------|--|
| `w` | Yes | Yes|`open("/path/to/file.txt","w")`|
| `a` | Yes | No (appends) |`open("/path/to/file.txt","a")`|
| `x` | Yes | No (raises error)|`open("/path/to/file.txt","x")`|
| `wb`| Yes | Yes|`open("/path/to/file.txt","wb")`|
| `ab`| Yes | No (appends) |`open("/path/to/file.txt","ab")`|
| `xb`| Yes | No (raises error)|`open("/path/to/file.txt","xb")`|


## `Exclusive Creation`
Exclusive creation creates a file for writing if it does not already exist, otherwise it raises an error. 
* `x` and `xb`

```python
try:
  with open("file.txt", "x") as file:
    file.write("Successful Creation")

except FileExistsError:
  print("File Already Exists")
```

<br>

[Back to Top](#python-file-handling)

___

<br>

# `Reading From Files`
When opening files with `open()` file contents can be read using the following modes:
* `r`,`rb`,`r+`,`rb+`

| Mode | Description | Notes|Example|
|---|--|--|--|
| `r`| Opens the file for reading (default mode). | File must exist, or an error is raised. |`open("/path/to/file.txt","r")`|
| `rb` | Opens the file for reading in binary mode. | Returns binary data (`bytes`).|`open("/path/to/file.txt","rb")`|
| `r+` | Opens the file for both reading and writing. | File must exist, or an FileNotFoundError is raised. |`open("/path/to/file.txt","r+")`|
| `rb+`| Opens the file for both reading and writing in binary mode.| File must exist or FileNotFoundError is raised; returns binary data. |`open("/path/to/file.txt","rb+")`|

<br>

File objects returned from `open()` can be read using the followindg methods:
* `.read()`,`.readline()`,`.readlines()`

<br>

---

`.read()` reads the entire content of a file, or up to a number of characters/bytes specified by `size` (default=-1 aka read the entire file).
* in text mode `size` refers to characters
* in binary mode `size` refers to bytes
* in binary mode returns a byte string

Syntax:
```
file.read(size=-1)
```
```python
with open("/path/to/file.txt", "r") as file:
  file.read()
```
```python
with open("/path/to/file.txt", "r") as file:
  file.read(size=4192)
```

---

<br>

`.readline()` reads one line from the file at a time, limiting the number of characters from each line using the `size` parameter (default=-1, read the whole line)
* calling `.readline()` subsequent times reads the next line
* in text mode `size` refers to characters
* in binary mode `size` refers to bytes
* in binary mode returns a byte string

<br>

Syntax:
```
file.readline(size=-1)
```
```python
with open("/path/to/file.txt", "r") as file:
  file.readline()
```
```python
with open("/path/to/file.txt", "r") as file:
  file.readline()
```

---

<br>

`.readlines()` reads each line of the file returning a list storing each line as a single element. 
* `sizehint` is the appoximate number of bytes to read (default=-1, read all lines)
* if read in binary mode, returns a list of byte strings

<br>

Syntax:
```
file.readlines(sizehint=-1)
```
```python
with open("/path/to/file.txt", "r") as file:
  file.readlines()
```
```python
with open("/path/to/file.txt", "r") as file:
  file.readlines(sizehint=4192)
```

<br>

[Back to Top](#python-file-handling)

___

<br>

# `Writing To Files`
*Be cautious when using `w`,`wb`, or `wb+` modes as they overwrite existing file content*

When opening files with `open()` file contents can be written to using the following modes:
* `w`,`a`,`x`
* add `b` to write using bytes
* add a `+` to read and write

| Mode   | Creates File? (If it doesn't exist) | Overwrites Existing?  | Allows Reading? | Example                           |
|--------|--------------------------------------|------------------------|-----------------|-----------------------------------|
| `w`    | Yes                                  | Yes                    | No              | `open("/path/to/file.txt", "w")`   |
| `a`    | Yes                                  | No (appends)           | No              | `open("/path/to/file.txt", "a")`   |
| `x`    | Yes                                  | No (raises error)      | No              | `open("/path/to/file.txt", "x")`   |
| `w+`   | Yes                                  | Yes                    | Yes             | `open("/path/to/file.txt", "w+")`  |
| `a+`   | Yes                                  | No (appends)           | Yes             | `open("/path/to/file.txt", "a+")`  |
| `x+`   | Yes                                  | No (raises error)      | Yes             | `open("/path/to/file.txt", "x+")`  |

<br>

| Mode   | Creates File? (If it doesn't exist) | Overwrites Existing?  | Allows Reading? | Example                           |
|--------|--------------------------------------|------------------------|-----------------|-----------------------------------|
| `wb`   | Yes                                  | Yes                    | No              | `open("/path/to/file.txt", "wb")`  |
| `ab`   | Yes                                  | No (appends)           | No              | `open("/path/to/file.txt", "ab")`  |
| `xb`   | Yes                                  | No (raises error)      | No              | `open("/path/to/file.txt", "xb")`  |
| `wb+`  | Yes                                  | Yes                    | Yes             | `open("/path/to/file.txt", "wb+")` |
| `ab+`  | Yes                                  | No (appends)           | Yes             | `open("/path/to/file.txt", "ab+")` |
| `xb+`  | Yes                                  | No (raises error)      | Yes             | `open("/path/to/file.txt", "xb+")` |


<br>

File objects returned from `open()` can be written to using the following methods:
* `.write()`, `.writelines()`

---

`.write()` writes a single string  specified by the `s` parameter to the file. 
* The function of `.write()` is dependant upon the mode specified with `open()`.
    * with `w` mode `.write()` trucates the file contents and write the new content.(ie. overwrite the file with new content)
    * with `a` mode `.write()` appends the new content to the end of the file.

Syntax:
```
file.write(s)
```
```python
with open("file.txt", "w") as file:
    file.write("Hello World, but inside a file!")

with open("file.txt", "a") as file:
    file.write("This is added to the end of the file")
```
---

<br>

`.writelines()` write a sequence of strings (list, tuple, generators, sets, custom iterables) specificed by the `lines` parameter to a file
* The function of `.writelines()` is dependant upon the mode specified with `open()`.
    * with `w` mode `.writelines()` trucates the file contents and write the new content.(ie. overwrite the file with new content)
    * with `a` mode `.writelines()` appends the new content to the end of the file.

Syntax:
```
file.writelines(lines)
```
```python
write_lines = [
    "This is the first line written with 'w' mode.\n",
    "This overwrites the existing content.\n"
] 

append_lines = [
    "This line is appended using 'a' mode.\n",
    "More content added to the existing file.\n"
]

with open("file.txt", "w") as file:
    file.writelines(write_lines)

with open("file.txt", "a") as file:
    file.writelines(append_lines)
```

<br>

[Back to Top](#python-file-handling)

___

<br>

# `Read and Write`
`+` can be used in conjuntion with other modes to read and write a file at the same time. 

| Mode   | File Creation | File Truncation | Writing Start Position | Special Notes                              |
|--------|---------------|-----------------|-------------------------|-------------------------------------------|
| `r+`,`rb+`   | No| No              | Current Position (Default is the Beginning)| Overwrites existing content from the start. |
| `w+`,`wb+`   | Yes| Yes             | Beginning               | File is cleared before writing.            |
| `a+`,`ab+`   | Yes| No              | End                     | Always appends to the end.                 |
| `x+`,`xb+`   | Yes| N/A             | Beginning               | Creates a new file, raises error if exists.|


`r+` or `rb+` modes do not delete the content of the file. These overwrite the content from the current pointer position in the file. 
*This means that if the size of the new data is less than the old, parts of the old data will remain*

Example
```python
with open("example.txt", "w") as file:
    file.write("Original Content")

# r+ mode (overwrite from start, no truncation)
with open("example.txt", "r+") as file:
    file.write("Updated")                # Overwrites 'Original' with 'Updated'
    print(file.read())                   # Output: l Content

with open("example.txt", "r") as file:
    print(file.read())                   # Output: Updatedl Content
```

<br>

`w+` or `wb+` modes truncate the contents of the file, place the pointer at position 0 and then overwrite.
```python
with open("example.txt", "w") as file:
    file.write("Original Content")

# w+ mode (truncate and overwrite)
with open("example.txt", "w+") as file: # Truncates and moves pointer to position 0
    file.read()                         # Output: 
    file.write("New Data")              # Writes 'New Data'

with open("example.txt", "r") as file:
    print(file.read())                  # Output: New Data
```

<br>

`a+` or `ab+` modes append contents to the end of the file.
* pointer is at the end of the file (aka the last byte of the file)

```python
with open("example.txt", "w") as file:
    file.write("Original Content")

# a+ mode (append without truncation)
with open("example.txt", "a+") as file:
    file.write(" - Appended")           # Appends at the end of the file

with open("example.txt", "r") as file:
    print(file.read())                  # Output: Original Content - Appended
```


<br>

[Back to Top](#python-file-handling)

___

<br>


# `File Pointers`

Basically: A `file pointer` is the spot where you are reading or writing to a file.

Specifically: A `file pointer` is a marker or indicator that keeps track of the current position (in bytes) in a file while it is being read from or written to. It determines where the next read or write operation will occur in the file.

<br>

To change the file pointer position using the file object returned by `open()`
| Method         | Description                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------|
| `file.seek(offset, whence=0)`   | Moves the file pointer to a specified position. `offset` is in bytes, and `whence` determines the reference point: |
|                               | - `0`: Start of the file (default)                                                               |
|                               | - `1`: Current pointer position                                                                  |
|                               | - `2`: End of the file                                                                           |
| `file.tell()`                 | Returns the current position of the file pointer in bytes.                                       |


Syntax
```
file.seek(offset, whence=0)
```
```python
with open("example.txt", "w") as file:
    file.write("abcdefghijklmnopqrstuvwxyz")
    file.seek(4)                        # Move to byte 4 ('d')
    file.write("5")                     # Write the next byte with "5"

with open("example.txt", "r") as file:
    print(file.read())                  # Output: abcde5ghijklmnopqrstuvwxyz
```

<br>

Syntax
```
file.tell()
```
```python
with open("example.txt", "w") as file:
    print(file.tell())      # Output: 0
    file.write("abcdefghijklmnopqrstuvwxyz")
    print(file.tell())      # Output: 26
    file.seek(4)
    print(file.tell())      # Output: 4

```

<br>

[Back to Top](#python-file-handling)

___

<br>

# `File Buffering and Flushing`
flush()
fileno()
isatty()

# `Error Handling`
try-except
Handle file exceptions using try...except blocks.

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

# `File Objects Overview`

| Attribute/Method      | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Attributes**        |                                                                                               |
| `file.closed`         | Returns `True` if the file is closed, `False` otherwise.                                      |
| `file.encoding`       | Returns the encoding used to decode or encode the file (e.g., `'UTF-8'`).                     |
| `file.mode`           | Returns the mode in which the file was opened (e.g., `'r'`, `'w'`, `'rb'`).                   |
| `file.name`           | Returns the name of the file.                                                                |
| `file.newlines`       | Returns the newline convention used (`None`, `\n`, `\r\n`, etc.).                            |
| `file.buffer`         | Returns the underlying binary buffer for the file.                                           |
| `file.line_buffering` | Returns `True` if line buffering is enabled (applies to text files only).                     |
| **Methods**           |                                                                                               |
| `file.close()`        | Closes the file. Further operations on the file will raise a `ValueError`.                   |
| `file.flush()`        | Flushes the write buffer to the disk.                                                        |
| `file.read(size=-1)`  | Reads up to `size` bytes (or the entire file if `size` is not specified or is `-1`).          |
| `file.readline(size=-1)` | Reads a single line from the file, up to `size` characters if specified.                  |
| `file.readlines(hint=-1)` | Reads all lines from the file and returns them as a list. The optional `hint` limits the total bytes read. |
| `file.seek(offset, whence=0)` | Moves the file pointer to a specific position: `offset` bytes from `whence`. `whence` can be: |
|                        | `0` (start of the file, default), `1` (current position), or `2` (end of the file).          |
| `file.tell()`         | Returns the current file pointer position in bytes.                                          |
| `file.truncate(size=None)` | Truncates the file to the specified size (default is the current file pointer position). |
| `file.write(string)`  | Writes a string to the file.                                                                 |
| `file.writelines(iterable)` | Writes a sequence of strings to the file.                                              |
| `file.readable()`     | Returns `True` if the file supports reading.                                                 |
| `file.writable()`     | Returns `True` if the file supports writing.                                                 |
| `file.seekable()`     | Returns `True` if the file supports random access (seeking).                                 |
| `file.detach()`       | Detaches the underlying buffer from the file. Only for binary files.                         |
| `file.fileno()`       | Returns the file descriptor (an integer) associated with the file.                           |
| `file.isatty()`       | Returns `True` if the file is connected to a terminal device.                                |
| `file.__iter__()`     | Returns an iterator over the file lines.                                                     |
| `file.__next__()`     | Returns the next line in the file when used with an iterator (`for line in file`).            |


