import read_csv
import id3

# Read in training file
try:
    (train_file, test_file) = read_csv.validate()
except ValueError:
    print("Exit program")
except IOError:
    print("Exit program")

train_data = read_csv.read(train_file)
test_data = read_csv.read(test_file)

try:
    read_csv.match(train_data, test_data)
except ValueError:
    print("Exit program")

# ID3 training
dt = id3.id3_train(train_data)
print("Learning finished, decision tree successfully built")
print("Start testing...")
# ID3 testing
new_filename = test_file[:-4]+"_id3.csv"
read_csv.write(new_filename, id3.id3_test(test_data, dt))
