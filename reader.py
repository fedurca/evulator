import os
import docx2txt
import re

# Define the directory path where the Docx files are stored
directory_path = "./works/"


# Create an empty list to store the GitHub links
github_links = []

# Traverse through the directory and read all Docx files
for filename in os.listdir(directory_path):
    if filename.endswith(".docx"):
        # Extract the text from the Docx file
        text = docx2txt.process(os.path.join(directory_path, filename))
        
        # Use regular expressions to find the GitHub links in the text
        matches = re.findall("(?P<url>https?://github.com/\S+)", text)
        
        # Append the matches to the list of GitHub links along with the filename
        for match in matches:
            github_links.append(f"{filename};{match}")

# Print the list of GitHub links with the filename separated by a semicolon
for link in github_links:
    print(link)