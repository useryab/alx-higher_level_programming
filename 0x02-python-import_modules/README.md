# Python Import Modules

what are modules? 
how to use them?
types of modules?

## Resources:book:

* [Modules in Python ](https://www.datacamp.com/tutorial/modules-in-python)
* []()

## The import statement

To use the functionality present in any module, you have to import it into your current program. You need to use the import keyword along with the desired module name. When interpreter comes across an import statement, it imports the module to your current program. You can use the functions inside a module by using a dot(.) operator along with the module name. First, let's see how to use the standard library modules. In the example below,math module is imported into the program so that you can use sqrt() function defined in it.

```python
import math             #You need to put this command,`import` keyword along with the name of the module you want to import
num = 4
print(math.sqrt(num))   #Use dot operator to access sqrt() inside module "math"
```

For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter, if it’s just one module you want to test interactively, use reload(), for example: reload(module_name).

## Writing Modules

Now that you have learned how to import a module in your program, it is time to write your own, and use it in another program. Writing a module is just like writing any other Python file. Let's start by writing a function to add/subtract two numbers in a file calculation.py.

```python
def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
```

If you try to execute this script on the command line, nothing will happen because you have not instructed the program to do anything. Create another python script in the same directory with name module_test.py and write following code into it.

```python
import calculation            #Importing calculation module
print(calculation.add(1,2))   #Calling function defined in add module.
```

If you execute module_test.py, you will see "3" as output. When the interpreter came across the import statement, it imported the calculation module in your code and then by using the dot operator, you were able to access the add() function.

More on Import Statements
There are more ways to import modules:

* from .. import statement
* from .. import * statement
* renaming the imported module
* from .. import statement

The from..import statement allows you to import specific functions/variables from a module instead of importing everything. In the previous example, when you imported calculation into module_test.py, both the add() and sub() functions were imported. But what if you only needed the add() function in your code?

Here is an example to illustrate the use of from..import

```python
from calculation import add
print(add(1,2))
```

In above example, only the add() function is imported and used. Notice the use of add()? You can now access it directly without using the module name. You can import multiple attributes as well, separating them with a comma in the import statement. Take a look at the following example:

```python
from calculation import add,sub
```

## from .. import * statement

You can import all attributes of a module using this statement. This will make all attributes of imported module visible in your code.

Here is an example to illustrate the use of from .. import *:

```python
from calculation import *
print(add(1,2))
print(sub(3,2))
```

Note that in the professional world, you should avoid using from..import and from..import*, as it makes your code less readable.

## Renaming the imported module

You can rename the module you are importing, which can be useful in cases when you want to give a more meaningful name to the module or the module name is too large to use repeatedly. You can use the as keyword to rename it. The following example explains how to use it in your program.

```python
import calculation as cal
print(cal.add(1,2))
```

You saved yourself some typing time by renaming calculation as cal.
Note that you now can't use calculation.add(1,2) anymore, as calculation is no longer recognized in your program.

## Module Search Path

You may need your modules to be used in different programs/projects and their physical location in the directory can be different. If you want to use a module residing in some other directory, you have some options provided by Python.
When you import a module named calculation, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named calculation.py in a list of directories given by the variable sys.path.
sys.path contains these locations:

the directory containing the input script (or the current directory).
PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
the installation-dependent default.
Assume module_test.py is in the /home/datacamp/ directory, and you moved calculation.py to /home/test/. You can modify sys.path to include /home/test/ in the list of paths, in which the Python interpreter will search for the module. For this, You need to modify module_test.py in following way:

```python
import sys
sys.path.append('/home/test/')

import calculation
print(calculation.add(1,2))
```

## Byte Compiled Files
Importing a module increases the execution time of programs, so Python has some tricks to speed it up. One way is to create byte-compiled files with the extension .pyc.
Internally, Python converts the source code into an intermediate form called bytecode, it then translates this into the native language of your computer and then runs it. This .pyc file is useful when you import the module the next time from a different program - it will be much faster since a portion of the processing required for importing a module is already done. Also, these byte-compiled files are platform-independent.
Note that these .pyc files are usually created in the same directory as the corresponding .py files. If Python does not have permission to write to files in that directory, then the .pyc files will not be created.

The dir() function
The dir() function is used to find out all the names defined in a module. It returns a sorted list of strings containing the names defined in a module.


import calculation
print(test.add(1,2))
print(dir(calculation))

 
Output:
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'sub']
In the output, you can see the names of the functions you defined in the module, add & sub. Attribute __name__ contains the name of the module. All attributes beginning with an underscore are default python attributes associated with a module.

**What you should learn from this project**

At the end of this project you are expected to be able to explain to anyone, without the help of Google:

Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
How to import functions from another file
How to use imported functions
How to create a module
How to use the built-in function dir()
How to prevent code in your script from being executed when imported
How to use command line arguments with your Python programs

**Exercises**

**0. Import a simple function from a simple file**

     Write a program that imports the function def add(a, b): from the file add_0.py and prints the result 
     of the addition 1 + 2 = 3

* You have to use print function with string format to display integers
* You have to assign:
  * the value 1 to a variable called a
  * the value 2 to a variable called b
  * and use those two variables as arguments when calling the functions add and print
  * a and b must be define in 2 different lines: a = 1 and another b = 2
* You can only use the word add_0 once in your code
* You are not allowed to use '*' for importing or __import__
* Your code should not be executed when imported


**1. My first toolbox!**

     Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

* Do not use the function print (with string format to display integers) more than 4 times
* You have to define:
     * the value 10 to a variable a
     * the value 5 to a variable b
     * and use those two variables only, as arguments when calling functions (included print)
     * a and b must be define in 2 different lines: a = 10 and another b = 5
* Your program should call each of the imported functions. See example bellow for format
     the word calculator_1 should be used only once in your file
* You are not allowed to use * for importing or '__import__'
* Your code should not be executed when imported

**2. How to make a script dynamic!**

Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no argument where passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (preferred in a near Future), if you know them you can use them.

3. Infinite addition

Write a program that prints the result of the addition of all arguments

The output should be the result of the addition of all arguments, followed by a new line
You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
Your code should not be executed when imported

4. Who are you?

Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

You should print one name per line, in alpha order
You should print only names that do not start with __
Your code should not be executed when imported

5. Everything can be imported

Write a program that imports the variable a from the file variable_load_5.py and prints its value.

You are not allowed to use * for importing or __import__
Your code should not be executed when imported
