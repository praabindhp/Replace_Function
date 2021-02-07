import csv

with open('linkedin - Base.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line[6])
        s1=line[6]
        f1=s1.replace()