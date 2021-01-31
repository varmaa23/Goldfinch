# Goldfinch


## Project title
Python Dictionary Input Sequence Matcher

## Project description
This project reads a .csv file with inputs (e.g. First Name, DOB) and matches each input value to a key in a predefined dictionary. Each key maps to an array of booleans that represent if encryption and/or masking should be applied. Each input value is matched to a key based on a matching algorithm that takes into account simple typos, case, acronyms, and some similar names/symbols. This program will extract the schema info from a postgres database and match the field names to the PIIs in the predefined dictionary. It will then return the encryption and masking information in dictionary form. 


## Tech/Framework used
Python

## Features
The matching algorithm uses Levenshtein distance to calculate the similarity between the input field and the key in the dictionary.

## Installation
All files should be placed in the same directory and run query_match.py (goldfinch/dictionary).


## Tests / How to Use?
Run query_match.py using the following statement:
python3 query_match.py

query_match.py expects a config.py file in the same directory where config.py contains the database's name, the username, and the password. 
The database have a table schema_info where schema_info has a column field_name. 

A sample schema_info.csv has been provided which can be copied into the postgresql table. 
