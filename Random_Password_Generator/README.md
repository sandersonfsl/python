## About This Project :

"This code will randomly generate a secure password based on how many characters the user want"

- What is a strong password ?

    * A password with 16 characters or more
    * A combination of letters, numbers and characters
    * A password shouldn't be shared, should be unique for each account or device


## Python Modules

- Python random Module :

    * A python built-in module to generate pseudo-random numbers

- Python random Module doc :

    * https://docs.python.org/3/library/random.html

- Example Python Random Module :

    * random.randrange()

    \# this method returns a randomly selected element from the range  created by the start, stop and step arguments.

    import random
    random.randrange(1, 50)

    >>> random.randrange(1, 50)
    2

    >>> random.randrange(0, 101, 10)
    80


- Python string Module :

    * A python built-in module that contains some constants, utility function and classes for string manipulation

- Example Python string Module :

    * string.ascii_letters 

    \# this line stores a string with all lowercase and uppercase letters

    import string
    print(string.ascii_letters)

    >>> print(string.ascii_letters)
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    

    * string.ascii_digits

    \# this line stores a string with all digits
    
    import string
    print(string.ascii_digits)

    >>> print(string.ascii_digits)
    0123456789


- Python string Module doc :

    * https://docs.python.org/3/library/string.html
    

## Why ?

- This programa is an easy to access code to generate strong password for any use



# Basic Instruction : 

    1. Edit file random_password_generator.py by putting the argument of the class Password as your password lenght (default configured to 16)

    2. Run the random_password_generator.py using Python

  