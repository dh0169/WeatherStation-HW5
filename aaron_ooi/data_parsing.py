#Converts a text file delimited by tabs to CSV, JSON, and XML format
import csv
import json
import xml.etree.ElementTree as ele_tree

file_path = r"C:\Users\Aaron O\Desktop\College\SJSU\Fall 2023\CMPE-131\CMPE131-TermProject\aaron_ooi"
file_name = input("Enter a file name: ")
format = input("Enter a format (c,j,x): ")
with open(file_path + "\\" + file_name, "r") as f:
    text = f.read()


def parse(format):
    if(format == "c"):  
        each_line = text.split("\n")
        header = each_line[0].split("\t")
        data = [header]
        for line in each_line[1:]:
            col_val = line.split("\t")
            data.append(col_val)
        with open(file_path+"\data.csv", "w", newline="") as out_file:
            writer = csv.writer(out_file)
            writer.writerows(data)
        print("Created a CSV file!")

    elif format == "j":
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
        print("Created a JSON file!")

    elif(format == "x"):
        each_line = text.split("\n")
        header = each_line[0].split("\t")
        rootElement = ele_tree.Element("data")
        for line in each_line[1:]:
            col_val = line.split("\t")
            player_ele = ele_tree.SubElement(rootElement, "player")
            for i, col in enumerate(col_val):
                header[i] = header[i].replace(" ", "_").replace("@", "").replace("-", "").replace("(", "").replace(")", "").replace("/", "")
                player_subele = ele_tree.SubElement(player_ele, header[i])
                player_subele.text = col_val
        xml_tree = ele_tree.ElementTree(rootElement)
        xml_path = r"C:\Users\Aaron O\Desktop\College\SJSU\Fall 2023\CMPE-131\CMPE131-TermProject\aaron_ooi\data.xml"
        xml_tree.write(xml_path)
        
        print("Created a XML file!")

    else:
        print("Invalid format!")

parse(format)