# GoodReads Best Books Data Ingestion and Analysis

## Project Overview
This project involves setting up a MySQL database, ingesting data from CSV files, normalizing the data to the Second Normal Form (2NF), and performing exploratory data analysis.

## Data Source
The data is sourced from GoodReads and contains information about books, authors, and genres.

## Database Setup
- MySQL database server is installed and running on localhost, port 3306.
- A new schema named 'new_schema' is created for this project.

## Data Normalization
- Data is normalized to 2NF to eliminate redundancy and ensure data integrity.
- Tables created: `books`, `authors`, `genres`.
- Relationships between tables are established using foreign keys.

## Data Ingestion
- Python script `import.py` is used to read CSV files and import data into MySQL.
- Data is inserted into the respective normalized tables.

## Exploratory Data Analysis
- SQL queries and Python scripts are used for data exploration.
- Analysis focuses on finding popular books, prolific authors, and common genres.

## Improvement Suggestions
- Implement indexing on frequently queried columns to enhance query performance.
- Consider MySQL partitions for handling larger datasets efficiently.
- Explore the possibility of using MySQL stored procedures for repeated complex operations.

## How to Run the Project
1. Ensure MySQL server is running and `new_schema` is created.
2. Update the CSV file paths in the Python script.
3. Run the Python script to create tables and import data.
4. Use SQL queries and Python for exploratory data analysis.

## Dependencies
- MySQL Server
- mysql-connector-python
- Python 3
- CSV files: `normalized_books.csv`, `normalized_authors.csv`, `normalized_genres.csv`

## Authors
Karolis Mickus