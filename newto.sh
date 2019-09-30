#!/bin/bash

FILE="$HOME/.whereto"


while test $# -gt 0; do
    case "$1" in 
        -h|--help)
            echo "$package - directory teleporter."
            echo "\nTeleport to a directory in which you have previously set a portal."
            echo "\n$package [args] [location]"
            echo "options:"
            echo "-a, --add         Adds a portal to the current directory in the index."
            echo "-e, --edit        Edit the index."
            echo "-h, --help        show usage."
            exit 0
            ;;
    esac
done

# translate the whole thing from python to bash.

# edit (open file in vim)

eval vim $FILE
exit 1
# add (pipe in the current directory)


# usage / help


# teleport 
