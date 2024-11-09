import pandas as pd

# Load the English and Tigrinya Bible CSV files
eng_bible_path = 'Datasets//Data_csv//english_bible.csv'
tig_bible_path = 'Datasets//Data_csv//tig_bible_verses.csv'

eng_bible_df = pd.read_csv(eng_bible_path)
tig_bible_df = pd.read_csv(tig_bible_path)

# Merge the dataframes on book_name, chapter_number, and verse_number
merged_bible_df = pd.merge(
    eng_bible_df, tig_bible_df,
    on=['book_name', 'chapter_number', 'verse_number'],
    suffixes=('_eng', '_tig')
)

# Save the merged dataframe to a new CSV file
output_merged_path = 'Datasets//Data_csv//merged_bible_verses.csv'
merged_bible_df.to_csv(output_merged_path, index=False)

print(f"The English and Tigrinya Bible verses have been successfully merged and saved to {output_merged_path}.")
