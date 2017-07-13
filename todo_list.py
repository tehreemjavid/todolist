"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    item = raw_input("What would you like to add? ")
    my_list.append(item)
    print "The add_to_list function has not yet been written"


def view_list(my_list):
    """Print each item in the list."""
    for item in my_list:
        print item



def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    while True:
        user_options = raw_input("""Would you like to:
     A. Add a new item 
     B. View list 
     C. Quit the program 
    """)
        if user_options == "A":
            add_to_list(my_list)
        elif user_options == "B":
            view_list(my_list)
        elif user_options == "C":
            break

#-------------------------------------------------

my_list = []
display_main_menu(my_list)
