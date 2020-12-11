from dictionary import matcher, getValue, getInputs
import sys

# Prints each field (not exact matches to the key) from the array and the corresponding field from the dictionary
def test1():
    testFields = ["firstname", "FirstName", "Phone #", "Telephone"]
    for field in testFields:
        key = matcher(field)
        print (field, ":", key)
    return

# Reads a .csv (fileName) file with a couple fields and matches the names with a key from the dictionary.
# It then prints the input field, its corresponding key, and the value of the key
def test2(fileName):
    inputs = getInputs(fileName)
    for input in inputs:
        key = matcher(input)
        print (input ,":", key,":", getValue(key))
    return


# To run test1(), no extra commandLine argument are needed. 
# To run test2(), write the names of the .csv file(s) that you want to read
    # e.g. SampleData.csv SampleData2.csv 
    # can use as many files as you want
def main(argv):
    if(len(argv) == 1):
        test1()
    else:
        for index in range(1, len(argv)):
            print("FILE:", argv[index])
            test2(argv[index])
            print("\n"*2)

if __name__ == "__main__":
    main(sys.argv)