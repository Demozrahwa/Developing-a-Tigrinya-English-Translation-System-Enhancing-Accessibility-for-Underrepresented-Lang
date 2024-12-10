import pandas as pd

# Load datasets
en_to_ti_df = pd.read_csv("/Capstone/Dataset_csv/en_to_ti_full_datasets.csv")
ti_to_en_df = pd.read_csv("/Capstone/Dataset_csv/ti_to_en_full_datasets.csv")

# Ensure the datasets have 'source' and 'target' columns
required_columns = {"source", "target"}
if not required_columns.issubset(en_to_ti_df.columns):
    raise ValueError("The 'en_to_ti' dataset must contain 'source' and 'target' columns.")
if not required_columns.issubset(ti_to_en_df.columns):
    raise ValueError("The 'ti_to_en' dataset must contain 'source' and 'target' columns.")

# Remove duplicate translation pairs
en_to_ti_cleaned = en_to_ti_df.drop_duplicates(subset=["source", "target"], keep="first")
ti_to_en_cleaned = ti_to_en_df.drop_duplicates(subset=["source", "target"], keep="first")

# Save cleaned datasets back to CSV
en_to_ti_cleaned.to_csv("/Capstone/Dataset_csv/en_to_ti_full_datasets.csv", index=False)
ti_to_en_cleaned.to_csv("/Capstone/Dataset_csv/ti_to_en_full_datasets.csv", index=False)

print("Duplicates removed and cleaned datasets saved.")
