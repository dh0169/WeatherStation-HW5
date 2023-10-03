#Converts a text file delimited by tabs to CSV, JSON, and XML format
import csv
import json
import xml
import pandas as pd

filename = input("Enter the file name: ")
format = input("Enter a format: ")

def parse(filename, format):
    if(format == 'c'):  
        # with open(filename, 'r') as r:
        #     reader = csv.reader(r,delimiter='\t')
        #     # for row in reader:
        #     #     print(row)
        # with open('test.csv', 'w', newline='') as w:
        #     writer = csv.writer(w)
        #     for rows in reader:
        #         writer.writerows(rows)
        csv_read = pd.read_csv(filename, delimiter='\t')
        csv_read.to_csv('test.csv', index=None)
    elif format == 'j':
        with open('test.json', 'w') as outfile,open(filename,'r') as f:
            data = json.load(f)
            json.dump(data,outfile,sort_keys=True)


parse(filename, format)