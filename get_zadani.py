import os
import docx2txt
import re

# Define the directory path where the Docx files are stored
directory_path = "./works/"

# Create an empty list to store the attributes
attributes_list = []

# Traverse through the directory and read all Docx files
for filename in os.listdir(directory_path):
    if filename.endswith(".docx"):
        # Extract the text from the Docx file
        text = docx2txt.process(os.path.join(directory_path, filename))
        
        # Extract the line starting with "Číslo a název:"
        line_cislo_nazev = ''
        for line in text.split('\n'):
            if line.startswith('Číslo a název:'):
                line_cislo_nazev = line.strip()
                break
    attributes_list.append(f"{filename};{line_cislo_nazev}")        
        # Extract the text between "Zadání:" and "Způsob zpracování:"
"""
        zadani_zpracovani = ''
        start_str = "Zadání:"
        end_str = "Způsob zpracování:"
        start_index = text.find(start_str)
        end_index = text.find(end_str)
        if start_index != -1 and end_index != -1:
            zadani_zpracovani = text[start_index + len(start_str):end_index].strip()
        
        # Append the attributes to the list along with the filename
"""

# Print the list of attributes with each attribute separated by a semicolon
for attributes in attributes_list:
    print(attributes)