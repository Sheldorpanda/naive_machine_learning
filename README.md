# naive_machine_learning
Written by Eric Lu. Naive machine learning based on ID3 and neural network, given training and testing files.

To use this program, the user needs a training data file and a testing data file, both in csv. The training file must cosnsist of n columns of attributes and 1 column of concept, while the testing file must consist of n columns of attributes to be learned.
With the shell script, run the program in console with the following command:
  ml.sh training.csv testing.csv
The program will take the first two command-line arguments as the training file and testing file. Once the files have correct formating, the program output two csv files, which are the learning results using ID3 and neural network approaches respecitvely.
