*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Multithreading`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

[Python3 Documentation](https://docs.python.org/3/)
<br>

___

<br>

Covered in this file:
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()


<br>

___

<br>

# `Sequentialism, Concurrency, and Parallelism`
| Concept         | Execution Style                       | Simultaneity       | Typical Use Case            | Complexity      |
|----------------|----------------------------------------|--------------------|------------------------------|-----------------|
| `Sequentialism`   | One task at a time, in order           | ❌ No               | Simple programs, scripts     | Low             |
| `Concurrency`     | Multiple tasks in progress (interleaved) | ⚠️ Maybe (interleaved, not simultaneous) | I/O-bound tasks, UI responsiveness | Medium          |
| `Parallelism`     | Multiple tasks at the same time         | ✅ Yes              | CPU-bound tasks, data processing | High            |

<br>

## `Sequentialism`
Basically: Sequentialism is the process of completing programming tasks one a time and step by step.

Specifically: `Sequentialism` is the process of executing tasks in a strict, linear order, with no overlap or simultaneous operations. 
* Each operation must complete fully before the next begins. 
* `Sequential programming` is where control flow is deterministic and single-threaded.

---

<br>

## `Concurrency`
Basically: `Concurrency` is the process of completing multiple programming tasks at the same time

Specifically: `Concurrency` is the ability of a system to make progress on multiple tasks by managing and interleaving their execution.

Concurrent Programs:
1. Tasks may not actually run at the same time, but may instead appear to progress together.
1. Coordinate tasks, possibly pausing one to run another (e.g. context switching or await/yeild)
1. Are typically implemented using threads, async/await, coroutines, or subprocesses.

---

<br>

## `Parallelism`

Basically: `Parallelism` is the process of performing multiple tasks at the exact same time. 

Specifically: `Parallelism` is a form of concurrency in which multiple operations or tasks are executed simultaneously, typically using multiple CPU cores, processors, or machines. 


Parallel programs:
1. Execute at the exact same time
1. Require multiple cores, processors, or CPUs
1. Are best used with CPU-bound tasks
1. Are best for independant tasks

<br>

[Back To Top](#multithreading)

___

<br>

# `Multithreading vs Multiprocessing vs Asynchoronous`

| Method           | Set-up Cost | Managed By   | Execution Model              | Memory Access         | Execution                        |
|------------------|-------------|--------------|------------------------------|------------------------|----------------------------------|
| `Multithreading` | Low         | Interpreter & OS | OS-level threads within one process | Shared memory space    | Concurrent (I/O-bound friendly)  |
| `Multiprocessing`| High        | OS           | Separate OS processes         | Separate memory spaces | Parallel (CPU-bound friendly)    |
| `Asynchronous`   | Low         | Interpreter  | Single thread + event loop    | Shared memory space    | Concurrent (I/O-bound optimized) |


||Threads|Processes|
|:-:|:-:|:-:|
|Set-up cost| Low| High|
|Handled by| Interpreter| OS|
|Memory Access| Shared| Separate Memory Space|
|Execution| Concurrent non-parallel| Concurrent Parallel|


Threads are concurrent, but not parallel. This means they cannot execute simultaneously, and instead are in progress at the same time, but are interleaved.



# `Bound Types in Program Performance`

| Bound Type    | Definition                                                                 | Best Concurrency Tool       | Why It Matters in Concurrency                              |
|---------------|----------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------|
| `I/O-bound`      | Task performance is limited by input/output operations like disk or network | `threading`, `asyncio`       | Concurrency lets CPU do other work while waiting on I/O     |
| CPU-bound      | Task performance is limited by computation speed and CPU usage            | `multiprocessing`            | True parallelism (multi-core) needed to improve speed       |
| `Memory-bound`   | Task performance is limited by memory access speed or memory size         | Depends (optimize memory use) | Performance gains come from optimizing memory layout/access |
| `Network-bound`  | Limited by data transfer speed over network connections                   | `asyncio`, `threading`       | Async/concurrency hides wait time from slow networks        |
| `Disk-bound`     | Limited by disk read/write speeds                                         | `threading`, `asyncio`       | Allows other tasks to run while waiting on disk operations  |

<br>


<br>

[Back To Top](#multithreading)

___

<br>

# `Locks`

A `race condition` occures when two or more threads or processes access shared data at the same time, and the final outcome depends on the timing or order of their execution. 
* race conditions can be prevent using `synchronization primitives`

<br>

A `synchronization primitive` is a low level building block provided by a programming language or OS to coordinate concurrent access to shared resources among threads or processes. 
* A `lock` is a synchronization primitive that ensures only one thread can access a particular critical section of code at a time. 

<br>

### `Types of Locks`
| Primitive            | Description                                                               | Key Methods                  | Typical Use Case                                 |
|----------------------|---------------------------------------------------------------------------|------------------------------|--------------------------------------------------|
| `Lock`               | Basic mutual exclusion lock (non-reentrant).                              | `acquire()`, `release()`     | Protect a critical section accessed by one thread at a time. |
| `RLock`              | Reentrant lock (a thread can acquire it multiple times).                  | `acquire()`, `release()`     | Recursive functions or nested locks in the same thread. |
| `Semaphore`          | Allows a limited number of threads to access a resource concurrently.     | `acquire()`, `release()`     | Resource pools (e.g., DB connections).           |
| `BoundedSemaphore`   | Like `Semaphore` but prevents exceeding initial count.                    | `acquire()`, `release()`     | Safer version of Semaphore for predictable limits. |
| `Condition`          | Used for waiting until a certain condition is true.                       | `wait()`, `notify()`, `notify_all()` | Complex coordination between threads.       |
| `Event`              | A flag used for signaling between threads.                                | `set()`, `clear()`, `wait()` | Thread communication and signaling.              |
| `Barrier`            | Blocks threads until a fixed number have reached the barrier.             | `wait()`                     | Synchronize threads at a certain point (e.g., start race together). |
| `Queue` (from `queue` module) | Thread-safe FIFO structure.                                             | `put()`, `get()`, `task_done()` | Producer-consumer patterns.                   |


<br>

## `Global Interpreter Lock GIL`
The `Global Interpreter Lock GIL` is a mutual exclusion lock (mutex) that protects access to Python objects preventing multiple native threads from executing Python bytecode at the same time in a single process. 
* Ensures thread safety for internal data structures
* prevents race conditions in memory managment

<br>




<br>

[Back To Top](#multithreading)

___

<br>


# `Creating Threads with Thread`
To create threads used the `threading` module .
* use the `Thread` class to instantiate new thread objects ie create threads.

<br>

Import the threading module:
```python
import threading
```

<br>

Create Thread objects with `Thread`

syntax:
```
threading.Thread(group = None, target = None, name = None, args = (), kwargs = {}, *, daemon = None)
```
* should always be called with keywords arguments.
* `group` is for a ThreadGroup class implementation
* `target` is a callable object invoked by the run() method
* `name` is the thread name
* `args` is a tuple set of arguments for target
* `kwargs` is a dictionary set of arguments for target
* `daemon` sets whether the thread is daemonic.

A `daemon` is a background thread or process that runs independently of the main program and automatically exits when all the non-daemon threads finish.

<br>

Example:
```python
import threading
import time

x = 0
def task():
    global x
    for num in range(10000):
        x = num
        time.sleep(0.1)


thread = threading.Thread(target = task, daemon = True)    # Create a Thread object (new thread)
thread.start()                                             # Start the thread's activity

run = True

while run:
    uin = input("Type some input: ")
    print(uin, x)
```

---

<br>

## `threading Functions`
This is not a complete list, just the common useful functions. 
Please see the Python documentation on Threading for a full list. 
[Python Threading](https://docs.python.org/3/library/threading.html)

<br>
```python
threading.active_count()
```
Return the number of currently active Thread objects

<br>

```python
threading.current_thread()
```
Return the current Thread object

<br>

```python
threading.excepthook(args,/)
```
Used for handling exceptions raised by the Thread.run() method

<br>

```python
threading.enumerate()
```
Returns a list of all Thread objects that are running.

<br>

```python
threading.main_thread()
```
Returns the main Thread object.

<br>

```python
threading.settrace(func)
```
Sets a trace function for the threads started from threading. func will be called before

___

<br>


# `Thread Instance Variables`

```python
thread.name
```
A string used for identification of a given thread.

<br>
<br>

```python
thread.ident
```
A non zero thread identifier integer. If the thread has not started this value is None.

<br>
<br>

```python
thread.native_id
```
A non-negative integer Thread ID (TID) assigned by the OS kernal. If the thread has not been started this value is None. 

<br>
<br>

```python
thread.daemon
```
A boolean value that indicates if the thread is running as a daemon.
* Must be set before `start()` is called. 

---

<br>



## `Thread Methods`

```python
thread.start()
```
Starts the thread and must be called once per thread object. 
* `run()` through this method using a control thread

<br>
<br>

```python
thread.run()
```
Represents the thread's activity. Typically, `run()` calls an objects constructor a the target argument including `args` and `kwargs`.

<br>
<br>

```python 
thread.join(timeout = None)
```
Waits until the given thread is finished executing. It blocks the calling thread until this thread terminates.
* when `timeout` is not None, it represent a floating point value for the timeout of the operation in seconds. Otherwise the operation blocks until the thread terminates.

<br>
<br>

```python
thread.is_alive()
```
Returns if the thread is alive, meaning it is still running. 



<br>

[Back To Top](#multithreading)

___

<br>

# `threading Lock`
The `threading.Lock` class implements primitive lock objects. 
* Once a thread has a lock attempt to acquire the lock are blocked.
* Once a lock is released other threads can acquire the lock.

<br>





# `Common Multithreading Problems`

Race Conditions

Deadlocks

Livelocks

Starvation

Wrong tool for the task

Overhead with Reduced Performance 

Resource Leaks

Non-Determinism


<br>

[Back To Top](#multithreading)

___

<br>

*Created and maintained by Mr. Merritt*