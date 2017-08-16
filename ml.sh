#!/bin/bash
echo "Machine learning, 2 csv files required"
echo "Please enter the training data csv, e.g.: train.csv, followed by [ENTER]:"
read train
echo "Please enter the testing data csv, e.g.: test.csv, followed by [ENTER]:"
read test
echo "Running..."
python3 ./__main__.py $train $test
echo "Done"
