
# Functions & Modules

- Functions
    - defining functions
    - parameters and arguements
    - returns
    - scope
    - built in functions

- Modules
    - importing
    - standard or built in modules
    - third party modules
    - aliasing

---

### But first review from last time...

- varaibles
    - define with meaningful names in snake case 🐍
    - can overwrite type and value at any time
    - can use screaming snake case (all caps) as a convention for a constant, but its only a convention

- math
    - integer and float data types
    - math operators: + - * / // % **
    - can use all of the above to assing += -= *=
    - / -> float.  & // -> integar

- help
    - using the build in `help` function


---


### Review (cont.)
    
- booleans
    - comparison operators: == != > < >= <= `is`
    - logical operators: and or is (need to talk more on this!)
    - use `is` when comparing True/False other times use `==`

- strings
    - single and multi line strings
    - indexing with strings `[start:stop:step]`


---

### Review (cont.)

- control flow
    - `if elif else` blocks to make choices
    - `while` or `for...in` loops to run code over and over
        - while loop stops based on a condition
        - for loop will 'visit' every item in a collection
    - can use `in` to check if something is in a collection



---

## Functions - Why should we use them?

- allow us to write code that we can reuse, hopefully many times
- helps to keep our code DRY, reusable, and more maintainable
- encapsulates the code of the function, once it written we just need to know what input is required and we get our output



---

### Python Functions

- We use the `def` keyword to define a function followed by:
    - The name of the function
    - The parameters that it accepts
    - A new block identified as `:` and indent the next line
    - We don't have to have a return value, but most often we will want one
    - If we don't define a return, python will default to returning `None`

```python=
# defining our function
def function_name(parameters):
    # function body

# calling our function
function_name(arguements)
```

---

### Parameters and Arguements

- parameters are like a variable that is going to get assigned the value of the arguements when they are passed in to the function call
- we can have positional or keyword arguements
- we can set default arguements too

```python=
# defining our function
def function_name(param_1, param_2):
    # function body

# calling our function
function_name(arg_1, arg_2)
function_name(param_2=arg_1, param_1=arg_2)
```

---


### Python Scoping

- Scoping is done at the function (and class) level
    - In JS, we had block scopes
    - In PY, our `if` statements do not create new scopes

```python=
def make_a_five():
    y = 5
    return y

if True:
    x = 10


print(x) #10
# `x` was created in the global scope

print(y) # NameError: name 'y' is not defined
# `y` was created in the scope of the make_a_five function
```

---

### Docstrings

A docstring is a string literal that is used to document a function, class, or module.

```python=
def my_function():
    """
    This is my function. It doesn't do
    anything special. It's just a
    function.
    """
    return 1
```

We can access docstrings in two ways:
```python=
help(my_function)
print(my_function.__doc__)
```

---

## Built in Functions

- we have access to these anywhere, we do not need to import them, they are pre defined functions that are not attached to a class as a method

- things like rounding, absolute value, sum, min, max, sorting, class constructors

- Oficial Python Documentation: https://docs.python.org/3.9/library/functions.html


---

### Popular Built In Functions

- `sum()`, `min()`, `max()`: get the sum, minimum value, or maximum value of a list of numerics
- `round()` and `abs()` for workin with integeras and floats
- `len()`: function that gets the length of an iterable
- `filter()`, `map()`, `enumerate()`, and `zip()` are used to manipulate lists, tuples, and sets (more in Module 3 about these)
- data type class constructors `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, and`dict()`


---


## sorted()

`sorted()` sorts any iterable data type. It returns a list of every element in the iterable in sorted order (using [Timsort](https://en.wikipedia.org/wiki/Timsort)).

`sorted()` takes two optional keyword arguments:
- `key`: a function that takes a single argument and returns a key to use for sorting
- `reverse`: a boolean value, if `True` the iterable will be sorted in reverse order

```python=
names = ["JAMES", "julie", "Ana", "Ria"]
sorted_names = sorted(names)
print(sorted_names)

# ensure a case-insensitive sort with the `.lower` string method 
# and sort in reverse order
sorted_names = sorted(names, key=str.lower, reverse=True)
print(sorted_names)
```

---




---



## Modules and Importing


---

To import code from a module, we use the `import` keyword. The import keyword will locate and initialize a module, and give you access to the specific names you have imported in the file.

There are no exports in Python! Anything we define in a module/file is automatically available for import.

---

### The `import` keyword
The Python standard library has a number of packages you can import without having to install them. Let's use the `random` package as an example (this would work the same with any package).

```python=
import random  # import everything from random
print(random.randint(0, 10))
```
Use the `as` keyword to alias package/object names.
```python=
import random as rand  # import everything, alias random as rand
print(rand.randint(0, 10))
```
You can also import specific objects from a package using the `from` keyword.

```python=
from random import randint, shuffle  # import multiple functions at the same time
print(randint(0, 10))
```

---


### Import Python code from another file
If two files are at the same level, import using the filename (without the `.py` extension).
```
project_folder
|  my_code.py
|  other_code.py
```

```python=
# inside my_code.py
import other_code
# import just a specific item
from other_code import my_function
```


---
