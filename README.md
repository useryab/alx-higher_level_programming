# alx-higher_level_programming 

## python Programming 101
[]()
[]()
[]()
[]()
### The python interpreter

 **Here's a breakdown of how the Python interpreter works:**

**1. Parsing and Tokenization:**

- The interpreter reads the Python source code (.py file).
- It breaks down the code into smaller elements called tokens, such as keywords, identifiers, operators, and literals.
- This process is called **tokenization**.

**2. Syntax Analysis and AST Generation:**

- The interpreter analyzes the tokens to ensure they follow Python's grammar rules.
- It creates a structured representation of the code called an **Abstract Syntax Tree (AST)**.
- The AST captures the relationships between different parts of the code.

**3. Bytecode Generation:**

- The interpreter converts the AST into a lower-level, platform-independent format called **bytecode**.
- Bytecode is a series of instructions that are specific to the Python virtual machine (PVM).
- Bytecode is stored in `.pyc` files for faster execution in subsequent runs.

**4. Virtual Machine Execution:**

- The **Python Virtual Machine (PVM)**, a software component of the interpreter, takes over.
- It reads the bytecode instructions and executes them one by one.
- It interacts with the underlying operating system to perform tasks like:
    - Managing memory
    - Handling input and output
    - Calling external libraries

**5. Dynamic Typing and Memory Management:**

- Python is dynamically typed, so data types are determined at runtime, not during compilation.
- The PVM manages memory for variables and objects during execution.
- It uses a technique called **garbage collection** to automatically reclaim memory that is no longer needed.

**Key Points:**

- The interpreter processes code line by line, from top to bottom.
- It allows for interactive coding and debugging.
- It's generally slower than compiled languages, but often more flexible and easier to develop with.
- The PVM is responsible for the actual execution of Python code.
- Bytecode files (`.pyc`) can speed up subsequent runs of the same code.

 **Here's a breakdown of the differences between `python -c` and `python -m`:**

**- `python -c`:**

- Executes a single Python statement or a series of statements as a string.
- Primarily used for quick one-liners or short blocks of code.
- Doesn't require creating a separate Python file.

**Example:**

```bash
python -c "print('Hello, world!')"
```

**- `python -m`:**

- Executes a module as a script.
- Treats the module's `__main__` block as the entry point.
- Useful for running modules that have their own functionality or for testing modules.

**Example:**

```bash
python -m my_module  # Runs the `my_module` module
```

**Key Differences:**

- **Purpose:** `-c` is for direct code execution, while `-m` is for running modules.
- **Input format:** `-c` takes a string of code, while `-m` takes a module name.
- **Entry point:** `-c` starts execution from the given code, while `-m` starts from the module's `__main__` block.

**When to Use Each:**

- Use `python -c` for:
    - Simple, one-off commands
    - Inline code testing
    - Exploring Python features interactively
- Use `python -m` for:
    - Running modules with their own functionality
    - Testing modules before installing them
    - Using modules as scripts

**Additional Notes:**

- Both options can be used from the command line or within scripts.
- They can be combined with other Python command-line options.
- For more complex code or long-term development, it's generally recommended to create Python files and run them using `python my_file.py`.

An Informal Introduction to Python
In the following examples, input and output are distinguished by the presence or absence of prompts (>>> and …): to repeat the example, you must type everything after the prompt, when the prompt appears; lines that do not begin with a prompt are output from the interpreter. Note that a secondary prompt on a line by itself in an example means you must type a blank line; this is used to end a multi-line command.

You can toggle the display of prompts and output by clicking on >>> in the upper-right corner of an example box. If you hide the prompts and output for an example, then you can easily copy and paste the input lines into your interpreter.

Many of the examples in this manual, even those entered at the interactive prompt, include comments. Comments in Python start with the hash character, #, and extend to the end of the physical line. A comment may appear at the start of a line or following whitespace or code, but not within a string literal. A hash character within a string literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.

Some examples:

```
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
3.1. Using Python as a Calculator
Let’s try some simple Python commands. Start the interpreter and wait for the primary prompt, >>>. (It shouldn’t take long.)

3.1.1. Numbers
The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be used for grouping. For example:

```
2 + 2
4
50 - 5*6
20
(50 - 5*6) / 4
5.0
8 / 5  # division always returns a floating point number
1.6
```
The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.

Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %:

>>>
17 / 3  # classic division returns a float
5.666666666666667

17 // 3  # floor division discards the fractional part
5
17 % 3  # the % operator returns the remainder of the division
2
5 * 3 + 2  # floored quotient * divisor + remainder
17
With Python, it is possible to use the ** operator to calculate powers 1:

>>>
5 ** 2  # 5 squared
25
2 ** 7  # 2 to the power of 7
128
The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

>>>
width = 20
height = 5 * 9
width * height
900
If a variable is not “defined” (assigned a value), trying to use it will give you an error:

>>>
n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

>>>
4 * 3.75 - 1
14.0
In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

'
tax = 12.5 / 100
price = 100.50
price * tax
12.5625
price + _
113.0625
round(_, 2)
113.06
This variable should be treated as read-only by the user. Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).

3.1.2. Text
Python can manipulate text (represented by type str, so-called “strings”) as well as numbers. This includes characters “!”, words “rabbit”, names “Paris”, sentences “Got your back.”, etc. “Yay! :)”. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2.

>>>
'spam eggs'  # single quotes
'spam eggs'
"Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
'1975'  # digits and numerals enclosed in quotes are also strings
'1975'
To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks:

>>>
'doesn\'t'  # use \' to escape the single quote...
"doesn't"
"doesn't"  # ...or use double quotes instead
"doesn't"
'"Yes," they said.'
'"Yes," they said.'
"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'
In the Python shell, the string definition and output string can look different. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:

>>>
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string
'First line.\nSecond line.'
print(s)  # with print(), special characters are interpreted, so \n produces new line
First line.
Second line.
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

>>>
print('C:\some\name')  # here \n means newline!
C:\some
ame
print(r'C:\some\name')  # note the r before the quote
C:\some\name
There is one subtle aspect to raw strings: a raw string may not end in an odd number of \ characters; see the FAQ entry for more information and workarounds.

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
produces the following output (note that the initial newline is not included):

Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
Strings can be concatenated (glued together) with the + operator, and repeated with *:

>>>
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
'unununium'
Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

>>>
'Py' 'thon'
'Python'
This feature is particularly useful when you want to break long strings:

>>>
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
'Put several strings within parentheses to have them joined together.'
This only works with two literals though, not with variables or expressions:

>>>
prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
If you want to concatenate variables or a variable and a literal, use +:

>>>
prefix + 'thon'
'Python'
Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

>>>
word = 'Python'
word[0]  # character in position 0
'P'
word[5]  # character in position 5
'n'
Indices may also be negative numbers, to start counting from the right:

>>>
word[-1]  # last character
'n'
word[-2]  # second-last character
'o'
word[-6]
'P'
Note that since -0 is the same as 0, negative indices start from -1.

In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain a substring:

>>>
word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

>>>
word[:2]   # character from the beginning to position 2 (excluded)
'Py'
word[4:]   # characters from position 4 (included) to the end
'on'
word[-2:]  # characters from the second-last (included) to the end
'on'
Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

>>>
word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:

>>>
word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
However, out of range slice indexes are handled gracefully when used for slicing:

>>>
word[4:42]
'on'
word[42:]
''
Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

>>>
word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
If you need a different string, you should create a new one:

>>>
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'
The built-in function len() returns the length of a string:

>>>
s = 'supercalifragilisticexpialidocious'
len(s)
34