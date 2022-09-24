#!/bin/bash

source .venv/bin/activate

if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python main.py
    else
        echo "Wrong version of python installed" >&2
    fi 
else
    echo "python not installed" >&2
fi


