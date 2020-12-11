# Goldfinch


## Project title
Python Dictionary Input Sequence Matcher

## Project description
This project reads a .csv file with inputs (e.g. First Name, DOB) and matches each input value to a key in a predefined dictionary. Each key maps to an array of booleans that represent if encryption and/or masking should be applied. Each input value is matched to a key based on a matching algorithm that takes into account simple typos, case, acronyms, and some similar names/symbols. 2 provided .csv files have also been provided (SampleData.csv and SampleData2.csv) as well as testCases.py, which tests the program. 


## Tech/Framework used
Python

## Features
The matching algorithm uses Levenshtein distance to calculate the similarity between the input field and the key in the dictionary.

## Installation
All files should be placed in the same directory.
Then, run testCases.py (e.g. /Users/aishwaryavarma/Desktop/goldfinch/dictionary/testCases.py) with the appropriate command-line arguments defined below. 

## Tests / How to Use?
There are 2 tests written in testCases.py. 

test1() uses a predefined array of potential inputs values (most of them aren't direct matches to the keys in the dictionary) and matches them to the keys. 
To use test1(), no commandLine arguments are needed.


test2() reads 1 or more csv files and prints the input values and the matching key. 
To use test2(), each commandLine argument should be the name of the .csv file, which should be in the directory. 
