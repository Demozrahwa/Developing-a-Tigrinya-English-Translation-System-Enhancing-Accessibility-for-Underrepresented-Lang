# Tigrinya-English Translation Project

This project focuses on building and fine-tuning machine translation models for Tigrinya-to-English and English-to-Tigrinya translations. The primary goal is to improve translation quality for underrepresented languages like Tigrinya using state-of-the-art models.

---

## Project Structure

- **Datasets**:
  - Datasets are stored in the `/content/drive/MyDrive/Capstone/Dataset_csv/` directory.
  - Includes `en_to_ti_full_datasets.csv` (English-to-Tigrinya) and `ti_to_en_full_datasets.csv` (Tigrinya-to-English).
  - The dataset contains over 90,000 sentences, with train-test splits and sample datasets for experimentation.

- **Models Used**:
  - **Helsinki-NLP/opus-mt-ti-en**: Used for Tigrinya-to-English translations.
  - **Helsinki-NLP/opus-mt-en-ti**: Used for English-to-Tigrinya translations.
  - **facebook/m2m100_418M**: A multilingual model for both directions.

- **Key Steps**:
  1. **Baseline Evaluation**: Measured BLEU scores using pre-trained models.
  2. **Fine-Tuning**: Trained the models on a 10% sample dataset for improved performance.
  3. **Evaluation**: Assessed performance on test datasets using BLEU and other metrics (e.g., chrF++ and COMET).

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
