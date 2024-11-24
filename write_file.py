import json
import  csv
from os import write

employees_csv = [
    ["Name", "Age", "Job"],
    ["Rabin", 27, "Software Developer"],
    ["Patrick", 32, "Unemployed"],
    ["Sandy", 42, "Scientist"]
]

employees_json = {
    "name" : " Rabin",
    "age" : "27",
    "job" :"Software Developer"
}

file_path = "/Users/rabinshah/Desktop/Vodafone bills/output.csv"

try:
    with open(file= file_path, mode="w", newline="") as file:
        # write json file
        # json.dump(employees_json, file, indent=4)

        # write csv file
        writer = csv.writer(file)
        for row in employees_csv:
            writer.writerow(row)
        print(f"csv file {file_path} was created")

except FileExistsError:
    print("That file already exists!")