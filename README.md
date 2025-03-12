# ETL Pipeline for Country-GDP Data

This project implements an ETL (Extract, Transform, Load) pipeline to process data about the largest banks and their market capitalization. The data is extracted from a Wikipedia page, transformed using exchange rates, and stored in both CSV and SQLite database formats.

## 🚀 Features
- Extracts bank market capitalization data from a Wikipedia page.
- Transforms data by converting market capitalization values into different currencies (USD, GBP, EUR, INR).
- Loads the transformed data into a CSV file and an SQLite database.
- Supports running SQL queries on the database.
- Logs the ETL process for tracking and debugging.

## 📂 Project Structure
```
SampleETL/
│── data/                      # Directory containing data files
│── etl.py                     # Main ETL script
│── exchange_rate.csv          # Exchange rate data
│── README.md                  # Project documentation
│── Banks.db                    # SQLite database storing processed data
│── Largest_banks_data.csv      # Processed data in CSV format
```

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/HoangCuong0811/SampleETL.git
   cd SampleETL
   ```

## 🛠 Usage
Run the ETL pipeline:
```bash
python src/etl.py
```
Alternatively, run specific steps separately:
```bash
python src/etl.py extract
python src/etl.py transform
python src/etl.py load
```

## 📜 ETL Process Details
### Extract
- Scrapes data from a Wikipedia page containing a list of the largest banks.
- Uses BeautifulSoup to parse the HTML and extract relevant table data.
- Saves extracted data into a Pandas DataFrame.

### Transform
- Reads exchange rate data from `exchange_rate.csv`.
- Converts market capitalization values from USD to GBP, EUR, and INR.
- Ensures proper data formatting and cleaning.

### Load
- Saves the transformed data into a CSV file (`Largest_banks_data.csv`).
- Stores the data in an SQLite database (`Banks.db`).
- Allows executing SQL queries for further analysis.

## 📌 System Requirements
- Python 3.x
- Required libraries (listed in `requirements.txt`):
  - pandas
  - numpy
  - requests
  - beautifulsoup4
  - sqlite3

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

