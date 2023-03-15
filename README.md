#### :keyboard: Python Projects


### RANDOM PASSWORD GENERATOR 

(Random_Password_Generator Folder)



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

    Output :

    2

    Output :

    80


- Python string Module :

    * A python built-in module that contains some constants, utility function and classes for string manipulation

- Example Python string Module :

    * string.ascii_letters 

    \# this line stores a string with all lowercase and uppercase letters

    import string
    print(string.ascii_letters)


    Output :

    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    

    * string.ascii_digits

    \# this line stores a string with all digits
    
    import string
    print(string.ascii_digits)

    Output :

    0123456789


- Python string Module doc :

    * https://docs.python.org/3/library/string.html
    

## Why ?

- This program is an easy to access code to generate strong password for any use



# Basic Instruction : 

    1. Edit file random_password_generator.py by putting the argument of the class Password as your password lenght (default configured to 16)

    2. Run the file random_password_generator.py using Python






### WRITE TO CSV 

(Write_to_CSV_File Folder)


## About This Project :

"The idea of this code is to write rows to a preset CSV file"

- What is a CSV file ?

    * A comma-separated-value file that has a specific format wich allows data to be saved in a table structured format.

- What is a CSV file used for ?

    * A way to store data that can be easily exchanged between programs


-  Example:

![CSV example](./python/Write_to_CSV_File/csv_example.png)

- Python CSV Module :
WRITE TO CSV 

    * https://docs.python.org/3/library/csv.html

    

## Why ?

- A simple interative way to write rows to a preseted with headers CSV file.



# Basic Instruction : 

    1. Firt define the headers of your CSV file in the preset file (preset_file.csv) structured like the default documment 

    2. Edit the headers list inside the write_to_csv.py file using your custom headers writed in preset_file.csv

    3. Run  write_to_csv.py using Python
