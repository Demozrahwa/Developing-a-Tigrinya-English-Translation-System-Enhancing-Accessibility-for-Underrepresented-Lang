# Tigrinya-English Translation Project

This project focuses on building and fine-tuning machine translation models for Tigrinya-to-English and English-to-Tigrinya translations. The primary objective is to enhance translation quality for underrepresented languages like Tigrinya by leveraging state-of-the-art machine learning models.

---

## Project Structure

- **Datasets**:
  - Datasets are located in the `/content/drive/MyDrive/Capstone/Dataset_csv/` directory.
  - Key files include:
    - `en_to_ti_full_datasets.csv` (English-to-Tigrinya)
    - `ti_to_en_full_datasets.csv` (Tigrinya-to-English)
  - Each dataset contains over 90,000 aligned sentences.
  - Train-test splits and sampled datasets are provided for experimentation.

- **Models Used**:
  - **Helsinki-NLP/opus-mt-ti-en**: Used for Tigrinya-to-English translations.
  - **Helsinki-NLP/opus-mt-en-ti**: Used for English-to-Tigrinya translations.
  - **facebook/m2m100_418M**: A multilingual model for both translation directions.
  - **t5-large**: Fine-tuned for translation tasks but demonstrated limited success.

- **Key Steps**:
  1. **Baseline Evaluation**: Assessed BLEU scores using pre-trained models as a benchmark.
  2. **Fine-Tuning**: Trained models on sampled datasets (10% of the full training set) to improve translation performance.
  3. **Evaluation**: Tested models on validation and test datasets using metrics such as BLEU, chrF++, and COMET.

---

## Installation

### Prerequisites
1. Python 3.9 or higher.
2. Libraries:
   - `transformers`
   - `datasets`
   - `evaluate`
   - `torch` (with CUDA support for GPU)

### Install Dependencies
```bash
pip install transformers datasets evaluate torch
