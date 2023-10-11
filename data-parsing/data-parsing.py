"""
Team: N.A.D.A

Python file to read input file "data.txt" and output 3 files in CSV, JSON, XML format

"""

import json
import csv
import xml.etree.ElementTree as ET

# Read the text file
file_path = "CMPE131-TermProject\data-parsing\data.txt"
with open(file_path, 'r') as file:
    text_data = file.read()

# Function to parse the text data with tab-separated values
def parse_data(option):
    if(option == "json"):
        lines = text_data.split('\n')
        header = lines[0].split('\t')
        data = []
        for line in lines[1:]:
            values = line.split('\t')
            player_data = {}
            for i, value in enumerate(values):
                player_data[header[i]] = value
            data.append(player_data)

        # Convert the parsed data to JSON
        json_data = json.dumps(data, indent=4)  # indent is optional for pretty formatting

        # Write the JSON data to a new file
        output_file_path = "CMPE131-TermProject\data-parsing\data-output.json"
        with open(output_file_path, 'w') as output_file:
            output_file.write(json_data)

        # Print the JSON data
        print(json_data)

    elif(option == "csv"):
        lines = text_data.split('\n')
        header = lines[0].split('\t')
        data = [header]

        for line in lines[1:]:
            values = line.split('\t')
            data.append(values)

        # Convert the parsed data to CSV
        output_file_path = "CMPE131-TermProject\data-parsing\data-output.csv"
        with open(output_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)

        print(f"Data has been written to {output_file_path}")

    elif(option == "xml"):
        lines = text_data.split('\n')
        header = lines[0].split('\t')

        # Create the root element for the XML
        root = ET.Element("data")

        for line in lines[1:]:
            values = line.split('\t')
            player_element = ET.SubElement(root, "player")

            for i, value in enumerate(values):
                # Replace or remove invalid characters from element names
                header[i] = header[i].replace(' ', '_').replace('@', '').replace(':', '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')
                field = ET.SubElement(player_element, header[i])
                field.text = value

        # Create the XML tree
        xml_tree = ET.ElementTree(root)

        # Save the XML to a file
        output_file_path = "CMPE131-TermProject\data-parsing\data-output.xml"  # Replace with the desired output XML file path
        xml_tree.write(output_file_path)

        # If you want to get the XML as a string, you can use the following line
        # xml_data = ET.tostring(root)

        # Print the XML data (optional)
        print(ET.tostring(root).decode('utf-8'))

# Get csv, json and xml output files
parse_data("csv")
parse_data("json")
parse_data("xml")
