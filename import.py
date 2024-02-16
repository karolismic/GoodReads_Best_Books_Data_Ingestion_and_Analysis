import mysql.connector
import csv

# Function to import CSV data to the MySQL database
def import_csv_to_table(csv_file_path, table_name, cursor, conn):
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        # Create table with TEXT columns for each header
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"""
            CREATE TABLE {table_name} (
            {', '.join(f"{header} TEXT" for header in headers)}
            )
        """)
        print(f"Table '{table_name}' created successfully.")

        # Prepare the INSERT INTO statement
        placeholders = ', '.join(['%s'] * len(headers))
        insert_statement = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})'
        # Insert the data into the table
        for row in reader:
            cursor.execute(insert_statement, row)
        conn.commit()
        print(f"Data imported successfully for {table_name}.")

try:
    # Connect to your MySQL DB
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="mysqlnow2024",
        database="new_schema" 
    )
    print("Connection to the MySQL database established successfully.")

    # Create a cursor object
    cur = conn.cursor()

    # Call the function to create tables and import data for each CSV file
    import_csv_to_table('normalized_books.csv', 'books', cur, conn)
    import_csv_to_table('normalized_authors.csv', 'authors', cur, conn)
    import_csv_to_table('normalized_genres.csv', 'genres', cur, conn)

except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")

except Exception as error:
    print(f"An error occurred: {error}")

finally:
    # Close the cursor and connection
    if cur is not None:
        cur.close()
        print("MySQL cursor closed.")
    if conn is not None and conn.is_connected():
        conn.close()
        print("MySQL connection closed.")
