#!/usr/bin/env python

import os
import sys

# initialize 
# maybe do another script.


def get_index():
    """
    returns the index path established by the $HOME
    variable.
    #TODO: look for a more effective / consistent / portable approach
    to this. may require a stateful(?) version of keeping the variable alive.

    RTRN --
    Returns a string of the path.

    ARGS --
    n/a
    """
    home = os.getenv("HOME")
    home += "/.whereto"
    return home


def transport(key):
    index = get_index()

    results = []
    f = open(index, 'r')
    for line in f:
        if key in line:
            results.append(line)


    res_count = len(results)
    if res_count == 0:
        print("There were no results available.")
        return 0
    elif res_count == 1:
        # GO
    elif res_count > 2 and res <= 9:
        i = 1
        print("[0] Cancel")
        for result in results:
            print(f"[{i}]: {result}")
            i += 1

        print("Which option would you like to travel to?")

        # guess we need to check whether it's python 2 or python3.
        # result = int(raw_input())
        result = int(input())

        if not result or type(result) != int:
            print("Invalid input.")
            return 0

        if result == 0:
            return 1

        if result > 0 and result < res_count:
            # GO result


    else:
        print("Too vague of a keyword - Clean the index or use a more specific keyword.")
        return 0


def go(path):
    """
    go will cd into the specified directory and minimize additional text.
    RTRN --
    Unknown

    ARGS --
    path - Takes a path as an argument to cd into.
    """



def add(entry):
    index = get_index()

    f = open(index, 'a+')
    f.write(entry)

    cwd = os.getcwd()
    f.close()


def edit():
    # simply open the file in vim.
    # if file doesn't exist - output error.


def remove():
    # Remove an argument in the python file.



def control():





if __name__ == '__main__':

    for arg in sys.argv:
        exe = []

        # if arg == '-a':
            # add

        # if arg == '-e':
            # edit

        # if arg == '-x':
            # remove

        # if arg is right then transport



