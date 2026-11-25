import csv

file = open("student.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(row)

file.close()

# OUTPUT
['Name', 'Roll No', 'Marks']
['Rahul', '101', '85']
['Sneha', '102', '90']
['Amit', '103', '78']
