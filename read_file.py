import json
import csv
# file_path = "/Users/rabinshah/Desktop/Vodafone bills/output.txt"
file_path = "/Users/rabinshah/Desktop/Vodafone bills/output.csv"

try:
    with open(file_path, mode="r") as file:
        # text file read
        # content = file.read()

        # json file read
        # content = json.load(file)

        #csv file read
        # print(content)
        content = csv.reader(file)
        for line in content:
            print(line[0])

except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
except IndexError:
    print("Outside index range")