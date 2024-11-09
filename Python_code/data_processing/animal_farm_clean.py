def clean_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []
    skip = False

    for line in lines:
        # Activate skip mode if line starts with "##"
        if line.startswith("##"):
            skip = True
            continue
        
        # Deactivate skip mode on reaching "OCR Results in This Page:"
        if "OCR Results in This Page:" in line:
            skip = False
            continue
        
        # Skip lines containing "---" and process other lines outside skip mode
        if not skip and "---" not in line:
            cleaned_line = line.strip()  # Remove leading/trailing whitespace
            if cleaned_line:  # Add only non-empty lines
                cleaned_lines.append(cleaned_line + '\n')  # Add newline for proper formatting
    
    # Write cleaned content to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)


input_file = 'Datasets//Data_txt//ሕርሻ እንስሳ.txt'
output_file = 'Datasets//Data_txt//cleaned_ሕርሻ እንስሳ.txt'
clean_text_file(input_file, output_file)

print("The text has been cleaned and saved to", output_file)
