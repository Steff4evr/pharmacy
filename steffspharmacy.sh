#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1

else 
    pip install pandas
    pip install time 2> /dev/null
    pip install clearing 2> /dev/null
    pip install openpyxl 2> /dev/null
    pip install re 2> /dev/null
    pip install rich 2> /dev/null
    pip install tabulate 2> /dev/null
    python src/steffs_pharmacy/main.py
fi


