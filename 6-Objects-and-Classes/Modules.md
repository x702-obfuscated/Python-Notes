#===============================================================================================================================#
'''Python Modules'''
#===============================================================================================================================#

'''
  Covered in this file:
  > Modules Defined
  > Importing
  > The Path
  > dir() function
  > if __name__ == "__main__":

'''

#https://docs.python.org/3/py-modindex.html

'> dir()'

dir() #lists the currently defined names ie (variables, modules, functions)

dir(__builtins__) #lists the builtin names


__main__ in Python is a special namespace or module name that refers to the scope in which top-level code is executed. It plays an important role when Python files are run as scripts or modules.

Here’s a detailed explanation of __main__:

1. __name__ and __main__
Every Python module (i.e., a Python file) has a special built-in variable called __name__.
When a Python script is run, the Python interpreter assigns the value '__main__' to the __name__ variable in that script.
If the script is imported as a module into another script, the __name__ variable is set to the module’s name (i.e., the filename without the .py extension).