
import pandas as pd
import re

import re
import csv

# Define the input and output file paths
input_file_path = 'TigrignaBible.txt'
cleaned_file_path = 'tig_bible_cleaned.txt'

## Regular expression to match lines that contain only a number
noise_pattern = re.compile(r'^\d{1,3}$')  # Matches lines with a single, double, or triple-digit number
# Regular expression to match chapter markers like "ምዕራፍ 1"
chapter_marker_pattern = re.compile(r'ምዕራፍ \d+')

# Read the file and process lines to remove noise
with open(input_file_path, 'r', encoding='utf-8') as file, open(cleaned_file_path, 'w', encoding='utf-8') as cleaned_file:
    lines = file.readlines()  # Read all lines in the file
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # If the line is a number-only noise line
        if noise_pattern.match(line):
            # Check if the second line is a potential book name and third line is a chapter marker
            if i + 2 < len(lines) and chapter_marker_pattern.match(lines[i + 2].strip()):
                # Skip only the number line (preserve book name and chapter marker)
                i += 1
            else:
                # Skip the number line and the following line
                i += 2
            continue
        
        # Write non-noise lines to the cleaned file
        cleaned_file.write(line + '\n')
        i += 1

print(f"Noise removed. Cleaned file saved as {cleaned_file_path}")