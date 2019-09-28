#!/usr/bin/env python
import pdb
import os
import sys

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
    """
    transport will find the

    RTRN --
    returns a 0 if there were no results or an error.
    returns a string if there was a successful read.
    ARGS --
    key - a string of the subsection that wants to be teleported to.
    """
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
        pass
    elif res_count > 2 and res <= 9:
        i = 1
        print("[0] Cancel")
        for result in results:
            print("[{}]: {}".format(i, result))
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
            pass

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
    # return thing
    pass


def add():
    """
    add will open the index file and write in the current directory.
    RTRN --
    Returns a 0.

    ARGS --
    n/a
    """
    index = get_index()
    f = open(index, 'a+')
    f.write(os.getcwd())
    f.close()
    return 0

def edit():
    """
    edit opens the file in vim
    RTRN --
    returns nothing.
    ARGS --
    n/a
    """
    # simply open the file in vim.
    # if file doesn't exist - output error.
    subprocess.run(["vim", get_index()])
    return

def remove():
    # Remove an argument in the python file.
    # Planned for future usage. Currently - use --edit

    # Open the file
    # Remove the instance - only if there is one such instance.
    pass

def usage():
    print("""
    WHERE TO. The directory teleporter.
    This tool is used to teleport to a different directory in a jiffy. \
    The idea is that you set 'portals' in directories you will be using frequently. \
    Once you want to teleport to a location, you can simply use the command line to get there.

    Usage: to <argument> [location]

    [location] should be the directory name you want to teleport to (or at least a part of it).

    Arguments:
    -a | --add  // Adds the current directory to the index.
    -e | --edit // Opens the index to edit.
    -h | --help // Pull up this usage screen.
    """)
    return


if __name__ == '__main__':
    for arg in sys.argv:
        if arg == '-a' or arg == '--add':
            add()
            break

        if arg == '-e' or arg == '--edit':
            edit()
            break

        if arg == '-h' or arg == '--help':
            usage()
            break
        """
        if arg == '-x':
            remove()
            break
        """

        #transport()
        # if arg is right then transport

