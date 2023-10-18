#Converts a text file delimited by tabs to CSV, JSON, and XML format
import csv
import json
import xml
import os

file_path = "CMPE131-TermProject\\aaron_ooi\\data.txt"
format = input("Enter a format (c,j,x): ")
with open(file_path, "r") as f:
    text = f.read()


def parse(filename, format):
    if(format == 'c'):  
        csv_read = pd.read_csv(filename, delimiter='\t')
        csv_read.to_csv('data.csv', index=None)
    elif format == 'j':
        each_line = text.split("\n")
        header = each_line[0].split("\t")
        data = []
        for line in each_line[1:]:
            col_val = line.split("\t")
            collection_data = {}
            for i, col in enumerate(col_val):
                #Store the entire row's data to collection_data
                collection_data[header[i]] = col
            #Finally, add the dict to list
            data.append(collection_data)
        json_format = json.dumps(data)
        with open(file_path+"\data.json", "w") as out_file:
            out_file.write(json_format)
        
    else:
        print("")

parse("data.txt", format)