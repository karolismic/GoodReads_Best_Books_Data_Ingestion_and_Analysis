# GoodReads Best Books Data Ingestion and Analysis

## Project Overview
This project sets up a SQLite database using SQLAlchemy, imports data from CSV files, normalizes the data, and prepares the foundation for future exploratory data analysis tasks.

## Data Source
The dataset originates from GoodReads and encompasses details about books, authors, and genres.

## Database Setup
- A SQLite database is utilized for this project due to its simplicity and ease of setup.
- SQLAlchemy, an Object-Relational Mapping (ORM) tool, is used to interact with the database using Python.

## Data Normalization
- The data is normalized to reduce duplication and enhance data integrity.
- The tables created include `books`, `authors`, and `genres`.
- Each table is structured with appropriate primary keys and datatypes.

## Data Ingestion
<<<<<<< HEAD
- The `main.py` Python script is developed to parse CSV files and populate the SQLite database.
=======
- The `import.py` Python script is developed to parse CSV files and populate the SQLite database.
>>>>>>> 69c79605c4d389272ce3d65316822e6e0545423e
- The script creates tables if they do not exist and inserts data into the respective tables.

## Exploratory Data Analysis
- Although not covered in this script, the setup allows for subsequent exploratory data analysis using SQL queries or Python-based data analysis tools.
- This analysis could include identifying trends among authors and genres, and discerning the most highly rated books.

## Improvement Suggestions
- Implement indexing on columns that are often used in search queries to improve performance.
- For larger datasets, consider transitioning to a more robust database system like PostgreSQL or MySQL.
- Integrate additional data sources for a more comprehensive analysis.

## How to Run the Project
1. Ensure Python is installed on your system.
2. Clone the repository and navigate to the project directory.
<<<<<<< HEAD
3. Run the `main.py` script to create the database and tables, and to import the data.
=======
3. Run the `import.py` script to create the database and tables, and to import the data.
>>>>>>> 69c79605c4d389272ce3d65316822e6e0545423e

After running the script, the database file my_database.db will be created and populated with data from the CSV files.

## Dependencies
- SQLAlchemy
- Pandas (for any data manipulation required during import)
- Python 3
- CSV files: `normalized_books.csv`, `normalized_authors.csv`, `normalized_genres.csv`

## Authors
Karolis Mickus