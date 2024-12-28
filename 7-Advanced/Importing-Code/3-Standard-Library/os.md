*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python os Module`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [``]()


<br>

___

<br>

# ``

<br>

[Back To Top](#python-os-module)

___

<br>

*Created and maintained by Mr. Merritt*








| **Category**            | **Attribute**                                         | **Description**                                                                                      |
|-------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **File and Directory**  | `os.getcwd()`                                       | Returns the current working directory.                                                              |
|                         | `os.chdir(path)`                                    | Changes the current working directory to the specified path.                                        |
|                         | `os.listdir(path)`                                  | Lists all entries in the specified directory.                                                       |
|                         | `os.mkdir(path)`                                    | Creates a new directory at the specified path.                                                      |
|                         | `os.makedirs(path)`                                 | Creates intermediate directories as needed.                                                         |
|                         | `os.remove(path)`                                   | Removes the specified file.                                                                         |
|                         | `os.rmdir(path)`                                    | Removes an empty directory.                                                                         |
|                         | `os.rename(src, dst)`                               | Renames a file or directory from `src` to `dst`.                                                    |
|                         | `os.replace(src, dst)`                              | Replaces the destination if it already exists.                                                      |
|                         | `os.path`                                          | Submodule for common path operations.                                                               |
| **File Descriptors**    | `os.open()`                                         | Opens a file and returns its file descriptor.                                                       |
|                         | `os.close(fd)`                                     | Closes the file descriptor.                                                                         |
|                         | `os.read(fd, n)`                                   | Reads `n` bytes from the file descriptor.                                                           |
|                         | `os.write(fd, data)`                               | Writes data to the file descriptor.                                                                 |
| **Environment**         | `os.environ`                                       | Dictionary object representing the environment variables.                                            |
|                         | `os.getenv(key, default=None)`                      | Gets an environment variable, with an optional default.                                             |
|                         | `os.putenv(key, value)`                            | Sets the value of an environment variable. (Deprecated, use `os.environ`.)                          |
|                         | `os.unsetenv(key)`                                 | Removes an environment variable.                                                                    |
| **Process Management**  | `os.getpid()`                                      | Returns the current process ID.                                                                     |
|                         | `os.getppid()`                                     | Returns the parent process ID.                                                                      |
|                         | `os.fork()`                                        | Creates a new process (Unix only).                                                                  |
|                         | `os.execv(path, args)`                             | Replaces the current process with a new one.                                                        |
|                         | `os.wait()`                                        | Waits for a child process to terminate.                                                             |
|                         | `os.kill(pid, sig)`                                | Sends a signal to the specified process.                                                            |
| **Platform Info**       | `os.name`                                          | Returns the name of the operating system-dependent module imported.                                 |
|                         | `os.uname()`                                       | Provides system information (Unix only).                                                            |
|                         | `os.cpu_count()`                                   | Returns the number of CPUs in the system.                                                           |
|                         | `os.getloadavg()`                                  | Returns the load average over 1, 5, and 15 minutes (Unix only).                                     |
|                         | `os.sysconf(name)`                                 | Returns system configuration information.                                                           |
| **File Metadata**       | `os.stat(path)`                                    | Returns file or directory information.                                                              |
|                         | `os.lstat(path)`                                   | Like `os.stat()`, but does not follow symbolic links.                                               |
|                         | `os.access(path, mode)`                            | Checks user's access permissions for the specified path.                                            |
| **Path Handling**       | `os.path.join()`                                   | Joins one or more path components intelligently.                                                    |
|                         | `os.path.split()`                                  | Splits a path into head and tail.                                                                   |
|                         | `os.path.exists()`                                 | Returns True if the path exists.                                                                    |
|                         | `os.path.isdir()`                                  | Returns True if the path is a directory.                                                            |
|                         | `os.path.isfile()`                                 | Returns True if the path is a file.                                                                 |
| **Signals and Errors**  | `os.strerror(code)`                                | Returns the string representation of a given error code.                                            |
|                         | `os.error`                                         | Alias for the built-in `OSError`.                                                                   |
|                         | `os.EX_*`                                          | Predefined exit codes (e.g., `os.EX_OK`, `os.EX_USAGE`, etc.).                                       |
| **Utilities**           | `os.urandom(n)`                                    | Returns `n` random bytes suitable for cryptographic use.                                            |
|                         | `os.linesep`                                       | String used to separate lines (`\n` on Unix, `\r\n` on Windows).                                     |
|                         | `os.sep`                                           | Separator used in file paths (`/` on Unix, `\\` on Windows).                                         |
|                         | `os.altsep`                                        | Alternate separator character (if available).                                                       |
|                         | `os.pathconf(path, name)`                          | Returns the value of a configuration option for the path.                                           |
