from sqlalchemy import create_engine, text
from contextlib import contextmanager
import csv

# A class encapsulates the database management code, enhancing modularity and reusability; it allows for cleaner organization of connection handling, making the codebase more maintainable.
# Using a class with a context manager for database connections ensures that resources are properly managed, opened, and closed, reducing the risk of connection leaks and making the code more robust.
# The class structure also improves scalability, as it makes it easier to extend functionality, such as adding connection pooling or supporting additional operations, without modifying the usage interface.
class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    @contextmanager
    def connect(self):
        """Provide a transactional scope around a series of operations."""
        connection = self.engine.connect()
        try:
            yield connection
        finally:
            connection.close()

# Function to import CSV data to the SQLite database
def import_csv_to_table(csv_file_path, table_name, db_manager):
    with db_manager.connect() as connection:
        with connection.begin():
            with open(csv_file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader)

                # Create table with TEXT columns for each header
                column_definitions = ', '.join([f'"{header}" TEXT' for header in headers])
                connection.execute(text(f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        {column_definitions}
                    )
                """))
                print(f"Table '{table_name}' created successfully.")

                # Prepare the INSERT INTO statement using named placeholders
                placeholders = ', '.join([f':{header}' for header in headers])
                insert_statement = text(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})')

                # Insert the data into the table
                for row in reader:
                    row_data = dict(zip(headers, row))
                    connection.execute(insert_statement, row_data)

                print(f"Data imported successfully for {table_name}.")

# Usage
db_manager = DatabaseManager('sqlite:///my_database.db')

try:
    import_csv_to_table('normalized_books.csv', 'books', db_manager)
    import_csv_to_table('normalized_authors.csv', 'authors', db_manager)
    import_csv_to_table('normalized_genres.csv', 'genres', db_manager)
except Exception as error:
    print(f"An error occurred: {error}")
