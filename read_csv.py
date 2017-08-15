import sys
import os
import csv

# .csv I/O
def read(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def write(file, data):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return

# Validate command line argument list
def validate():
    if len(sys.argv) < 2:
        raise ValueError("Invalid number of input")

    train_file = sys.argv[0].trim()
    test_file = sys.argv[1].trim()

    if train_file[-4:] != ".csv" or test_file[-4:] != ".csv":
        raise ValueError("Invalid input format, both files should be in .csv ")

    if (not os.path.isfile(train_file)) or (not os.path.isfile(test_file)):
        raise IOError("Training data or testing data file not found")

    return train_file, test_file

# Validate file format
def match(train_data, test_data):
    if len(train_data[0]) != (len(test_data[0]) + 1):
        raise ValueError("Param number do not match")
    return
