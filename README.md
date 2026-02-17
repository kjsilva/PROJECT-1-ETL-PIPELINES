
# PROJECT-1-ETL-PIPELINES

## Overview
This project implements a complete ETL (Extract, Transform, Load) pipeline using Python. It scrapes datasets from the web, processes and cleans the data, and loads it into a MySQL database. The project also exposes a FastAPI server to serve the processed data via a REST API.

## Features
- **Web Scraping**: Automated download of datasets from public sources using BeautifulSoup and requests.
- **Data Cleaning**: Cleans and transforms raw data using pandas and regex.
- **Database Integration**: Loads cleaned data into a MySQL database using SQLAlchemy.
- **API Server**: FastAPI-based server to provide access to the data.
- **Credential Encryption**: Secure handling of database credentials using cryptography.

## Project Structure

```
CODEBASE/
  api_server.py         # FastAPI server exposing data endpoints
  data_scraper.py       # Scraper class for downloading datasets
  dataset_scraper.ipynb # Jupyter notebook for stepwise ETL demonstration
  db_cred.py            # Credential encryption/decryption utilities
  db_engine.py          # SQLAlchemy engine setup using encrypted credentials
  enccred.env           # Encrypted database credentials
  func.py               # Data import and cleaning functions
  sql_loader.py         # SQL table creation and loading utilities
FILES/
  samp_csv.csv          # Sample dataset (scraped and processed)
README.md               # Project documentation
```

## Setup Instructions
1. **Clone the repository** and navigate to the project directory.
2. **Set up a Python virtual environment** (recommended):
	```bash
	python -m venv venv
	source venv/Scripts/activate  # On Windows
	```
3. **Install dependencies**:
	```bash
	pip install -r requirements.txt
	```
4. **Configure Database Credentials**:
	- Edit `CODEBASE/enccred.env` with your MySQL credentials (encrypted).
	- Use `db_cred.py` to encrypt/decrypt credentials as needed.
5. **Run the ETL Pipeline**:
	- Use `dataset_scraper.ipynb` for a step-by-step ETL process.
	- Or run scripts in `CODEBASE/` for automated execution.
6. **Start the API Server**:
	```bash
	uvicorn CODEBASE.api_server:app --reload
	```

## Usage
- **Scraping Data**: `data_scraper.py` downloads and saves datasets to the `FILES/` directory.
- **Cleaning Data**: `func.py` provides functions to clean and standardize the dataset.
- **Loading Data**: `sql_loader.py` creates tables and loads data into MySQL.
- **API Access**: Access data via `GET /cars_data?limit=10` endpoint.

## Key Files Explained
- **api_server.py**: FastAPI app exposing `/cars_data` endpoint to fetch data from MySQL.
- **data_scraper.py**: Contains `Scraper` class to automate dataset download from data.gov.
- **func.py**: Functions for importing CSVs and cleaning data (renaming columns, handling missing values, etc.).
- **sql_loader.py**: Generates SQL table creation scripts based on DataFrame structure.
- **db_engine.py**: Reads encrypted credentials, decrypts them, and creates a SQLAlchemy engine.
- **db_cred.py**: Utilities for encrypting and decrypting database passwords using Fernet and AES.
- **enccred.env**: Stores encrypted credentials and DB connection info.
- **dataset_scraper.ipynb**: Jupyter notebook for interactive ETL demonstration.

## Security
- Credentials are encrypted using Fernet/AES and stored in `enccred.env`.
- Decryption is handled at runtime by `db_cred.py` and `db_engine.py`.

## Requirements
- Python 3.8+
- MySQL Server
- Required Python packages: requests, beautifulsoup4, pandas, sqlalchemy, fastapi, uvicorn, cryptography, pycryptodome

## Example API Request
Fetch 5 rows from the cars table:
```
GET http://127.0.0.1:8000/cars_data?limit=5
```

## License
MIT License


