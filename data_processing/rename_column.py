# Importing the pandas library f
import pandas as pd 

# Reading the full dataset from a CSV file into a pandas DataFrame
eng_df = pd.read_csv('/Capstone/Dataset_csv/full_datasets.csv')


# List of relevant columns to be renamed (English and Tigrinya text columns)
lst = ['verse_text_eng', 'verse_text_tig']

# Renaming columns for English to Tigrinya translation and saving to a new CSV file
en_ti_df = eng_df.rename(columns={'verse_text_eng': 'Source', 'verse_text_tig': 'Target'})
en_ti_df.to_csv('./Capstone/Dataset_csv/en_to_ti_full_datasets.csv')

# Renaming columns for Tigrinya to English translation and saving to a new CSV file
ti_en_df = eng_df.rename(columns={'verse_text_tig': 'Source', 'verse_text_eng': 'Target'})
ti_en_df.to_csv('/Capstone/Dataset_csv/ti_to_en_full_datasets.csv')

# Displaying the first few rows of the Tigrinya-to-English DataFrame to verify the data
ti_en_df.head()
