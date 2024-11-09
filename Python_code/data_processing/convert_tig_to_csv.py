bible_chap_map = {
    "x":"y",
    'Genesis': 'ኦሪት ዘፍጥረት',
    'Exodus': 'ኦሪት ዘጸአት',
    'Leviticus': 'ኦሪት ዘሌዋውያን',
    'Numbers': 'ኦሪት ዘህልቍ',
    'Deuteronomy': 'ኦሪት ዘዳግም',
    'Joshua': 'መጽሓፍ ኢያሱ',
    'Judges': 'መጽሓፍ መሳፍንቲ',
    'Ruth': 'መጽሓፍ ሩት',
    '1 Samuel': '1 ሳሙኤል',
    '2 Samuel': '2 ሳሙኤል',
    '1 Kings': '1 ነጋሲ',
    '2 Kings': '2 ነጋሲ',
    '1 Chronicles': '1ይ ዜና መዋአል',
    '2 Chronicles': '1ይ ዜና መዋአል',
    'Ezra': 'መጽሓፍ  ዕዝራ',
    'Nehemiah': 'መጽሓፍ  ነህምያ',
    'Esther': 'መጽሓፍ ኣስቴር',
    'Job': 'መጽሓፍ  ኢዮብ',
    'Psalms': 'መዝሙር ዳዊት',
    'Proverbs': 'መጽሓፍ  ምሳሌ',
    'Ecclesiastes': 'መጽሓፍ መክብብ',
    'Song of Solomon': 'መኃልየ መኃልየ',
    'Isaiah': 'ትንቢት ኢሳይያስ',
    'Jeremiah': 'ትንቢት ኤርምያስ',
    'Lamentations': 'ሰቆቃው ኤርምያስ',
    'Ezekiel': 'ትንቢት ሕዝቅኤል',
    'Daniel': 'ትንቢት ዳንኤል',
    'Hosea': 'ትንቢት ሆሴዕ',
    'Joel': 'ትንቢት ኢኦኤል',
    'Amos': 'ትንቢት አሞጽ',
    'Obadiah': 'ትንቢት አብድዩ',
    'Jonah': 'ትንቢት ዮናስ',
    'Micah': 'ትንቢት ሚክያስ',
    'Nahum': 'ትንቢት ናሆም',
    'Habakkuk': 'ትንቢት ዕንባቆም',
    'Zephaniah': 'ትንቢት ሶፎንያስ',
    'Haggai': 'ትንቢት ሐጌ',
    'Zechariah': 'ትንቢት ዘካርያስ',
    'Malachi': 'ትንቢት ማላክያስ',
    'Matthew': 'ወንጌል ማቴዎስ',
    'Mark': 'ወንጌል ማርቆስ',
    'Luke': 'ወንጌል  ሉቃስ',
    'John': 'ወንጌል ዮሐንስ',
    'Acts': 'ግብረ ሐዋርያት',
    'Romans': 'መልእኽቲ ፓውሎስ ናብ ሰብ ሮሜ',
    '1 Corinthians': '1ይ መልእኽቲ ፓውሎስ ናብ ሰብ ቆሮንቶስ',
    '2 Corinthians': '2ይ መልእኽቲ ፓውሎስ ናብ ሰብ ቆሮንቶስ',
    'Galatians': 'መልእኽቲ ፓውሎስ ናብ ሰብ ገላትያ',
    'Ephesians': 'መልእኽቲ ፓውሎስ ናብ ሰብ ኤፌሶን',
    'Philippians': 'መልእኽቲ ፓውሎስ ናብ ሰብ ፊልጵስዩስ',
    'Colossians': 'መልእኽቲ ፓውሎስ ናብ ሰብ ቆላስይስ',
    '1 Thessalonians': '1ይ መልእኽቲ ፓውሎስ ናብ ሰብ ተሰሎንቄ',
    '2 Thessalonians': '2ይ መልእኽቲ ፓውሎስ ናብ ሰብ ተሰሎንቄ',
    '1 Timothy': '1ይ መልእኽቲ ፓውሎስ ናብ ሰብ ጢሞቴዎስ',
    '2 Timothy': '2ይ መልእኽቲ ፓውሎስ ናብ ሰብ  ጢሞቴዎስ',
    'Titus': 'መልእኽቲ ፓውሎስ ናብ ሰብ ቲቶ',
    'Philemon': 'መልእኽቲ ፓውሎስ ናብ ሰብ ፊልሞን',
    'Hebrews': 'መልእኽቲ ፓውሎስ ናብ ሰብ ዕብራውያን',
    'James': 'መልእኽቲ ያዕቆብ',
    '1 Peter': '1ይ መልእኽቲ ጴጥሮስ',
    '2 Peter': '2ይ መልእኽቲ ጴጥሮስ',
    '1 John': '1ይ መልእኽቲ ዮሐንስ',
    '2 John': '2ይ መልእኽቲ ዮሐንስ',
    '3 John': '3ይ መልእኽቲ ዮሐንስ',
    'Jude': 'መልእኽቲ ይሁዳ',
    'Revelation': 'ራእይ ዮሐንስ'
}

import pandas as pd
import re

import re
import csv

# Define the input and output file paths
# Define the input and output file paths
cleaned_file_path = 'tig_bible_cleaned.txt'
output_csv_path = 'tig_bible_verses.csv'


# Regular expression to match chapter markers and verse numbers
chapter_number_pattern = re.compile(r'ምዕራ ፍ (\d+)')  # Matches chapter number lines like "ምዕራፍ 1"
verse_split_pattern = re.compile(r'(\d+)\s')  # Matches a verse number followed by a space

# Initialize variables to store the current book, chapter, and verses
current_book = list(bible_chap_map.keys())[0]  # Start with the first book
current_chapter = None
verses = []  # List to store each verse as a dictionary

# Read the entire text file content
with open(cleaned_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Split content by chapter markers
chapters = chapter_number_pattern.split(content)

# Initialize an iterator for book names (starting from the second book onward)
book_names = iter(list(bible_chap_map.keys())[1:])

# Process each chapter section
for i in range(1, len(chapters), 2):
    chapter_text = chapters[i + 1]
    chapter_number = int(chapters[i].strip())  # Extract the chapter number

    # Check if it's the start of a new book (when chapter 1 appears)
    if chapter_number == 1:
        # Move to the next book name if available
        current_book = next(book_names, current_book)
    
    # Split chapter text by verse numbers and extract verses
    verse_segments = verse_split_pattern.split(chapter_text)
    
    # Process verse segments
    for j in range(1, len(verse_segments), 2):
        verse_number = int(verse_segments[j].strip())
        verse_text = verse_segments[j + 1].strip().replace('\n', ' ')  # Ensure verse text is in a single line

        # Append to verses list
        verses.append({
            'book_name': current_book,
            'chapter_number': chapter_number,
            'verse_number': verse_number,
            'verse_text': verse_text
        })

# Writing to the CSV file
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as csvfile:
    # Define the fieldnames
    fieldnames = ['book_name', 'chapter_number', 'verse_number', 'verse_text']
    
    # Initialize the CSV writer
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write each verse to the CSV file
    for verse in verses:
        writer.writerow({
            'book_name': verse['book_name'],
            'chapter_number': verse['chapter_number'],
            'verse_number': verse['verse_number'],
            'verse_text': verse['verse_text']
        })

print(f"Data has been successfully written to {output_csv_path}")