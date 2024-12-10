# Tigrinya-English Translation System

## Project Overview
This project focuses on developing a machine translation system between Tigrinya and English. Tigrinya, a low-resource language spoken in Eritrea and Ethiopia, has limited digital tools for linguistic support. The project leverages transformer-based models such as Helsinki-NLP and M2M100, fine-tuned on a custom dataset of over 350,000 bilingual sentence pairs.

---

## Features
- **Tigrinya-to-English Translation:** Translate Tigrinya sentences into English accurately.
- **English-to-Tigrinya Translation:** Translate English sentences into Tigrinya.
- **Custom Fine-Tuning:** Fine-tuned pre-trained models to improve translation quality using a diverse dataset.


---

## File Structure

Capstone/
│
├── Dataset_csv/
│   ├── en_to_ti_sampled_test.csv          # Sampled English-to-Tigrinya test dataset
│   ├── en_to_ti_sampled_train.csv         # Sampled English-to-Tigrinya training dataset
│   ├── ti_to_en_sampled_train.csv         # Sampled Tigrinya-to-English training dataset
│   ├── ti_to_en_sampled_val.csv           # Sampled Tigrinya-to-English validation dataset
│   ├── en_to_ti_val.csv                   # Full English-to-Tigrinya validation dataset
│   ├── ti_to_en_val.csv                   # Full Tigrinya-to-English-to-validation dataset
│   ├── ti_to_en_test.csv                  # Full Tigrinya-to-English test dataset
│   ├── en_to_ti_test.csv                  # Full English-to-Tigrinya test dataset
│   ├── en_to_ti_train.csv                 # Full (English-to-Tigrinya) training dataset 
│   ├── ti_to_en_train.csv                 # Full (Tigrinya-to-English) training dataset
│
├── models/
│   ├── m2m100_model.ipynb                 # M2M100 model notebook
│   ├── En_Ti_Helsinki-NLP_model.ipynb     # Helsinki-NLP model notebook (English to Tigrinya)
│   ├── Ti_En_Helsinki-NLP_model.ipynb     # Helsinki-NLP model notebook (Tigrinya to English)
|   |── T5_model.ipynb                     # T5_BERT model
|
│── opus-mt-en-ti_fine_tuned/             # Fine-tuned Helsinki-NLP model (English-to-Tigrinya)
│── opus-mt-ti-en_fine_tuned/             # Fine-tuned Helsinki-NLP model (Tigrinya-to-English)
│── t5_large_fine_tuned_model/            # Fine-tuned T5 model
|
data_processing/
│   ├── clean_txt.py                       # Script to clean raw text files
│   ├── combine_eng_tig.py                 # Script to combine English and Tigrinya datasets
│   ├── convert_tig_to_csv.py              # Convert raw Tigrinya text to CSV format
│   ├── remove_duplicates_translation_pairs.py # Script to remove duplicate translations
│   ├── rename_column.py                   # Rename columns in CSV files
│   ├── PDF_to_text.py                     # OCR conversion from PDF to text
│
├── README.md                              # Project README
├── requirements.txt                       # Python dependencies
|                           

## How to Run the Project

### Step 1: Clone the Repository
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/tigrinya-translation.git
cd tigrinya-translation
