*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python Streams`
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

[Back To Top](#python-decorators)

___

<br>

*Created and maintained by Mr. Merritt*

When our program starts, the three streams are already opened and don't require any extra preparations. What's more, your program can use these streams explicitly if you take care to import the sys module:

sys.stdin
stdin (as standard input)
the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
the well-known input() function reads data from stdin by default.

sys.stdout
stdout (as standard output)
the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
the well-known print() function outputs the data to the stdout stream.

sys.stderr
stderr (as standard error output)
the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work;
we haven't presented any method to send the data to this stream (we will do it soon, we promise)
the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.