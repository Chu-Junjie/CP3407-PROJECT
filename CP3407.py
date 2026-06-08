import os
import sqlite3
import pandas as pd


def setup_and_query_database():
    csv_filename = "US-02 Database Setup & Import.csv"
    db_filename = "digital_products.db"
    table_name = "products"

    # Ensure the target CSV dataset exists
    if not os.path.exists(csv_filename):
        print(f"[ERROR] Source file '{csv_filename}' not found. Please place it in the same directory.")
        return

    print("=== [AC 2] Initializing Local Database Instance ===")
    # Creating or connecting to the SQLite database instance (Fulfills AC 2)
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    print(f"[SUCCESS] Database instance '{db_filename}' successfully created locally.")

    print("\n=== [AC 3] Importing CSV Dataset into Database Table ===")
    try:
        # Load the cleaned dataset using pandas
        dataframe = pd.read_csv(csv_filename)

        # Write the dataframe records directly into SQL table (Fulfills AC 3)
        dataframe.to_sql(table_name, connection, if_exists="replace", index=False)
        connection.commit()

        # Verify row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        total_rows = cursor.fetchone()[0]
        print(f"[SUCCESS] Imported {total_rows} product records into table '{table_name}' successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to import dataset into table: {e}")
        connection.close()
        return

    print("\n=== [AC 4] Executing Backend Query Script (Testing 5 Records) ===")
    try:
        # Simple SQL Query to select the first 5 records (Fulfills AC 4)
        query_sql = f"SELECT ProductID, ProductCategory, ProductBrand, ProductPrice FROM {table_name} LIMIT 5;"
        cursor.execute(query_sql)
        fetched_records = cursor.fetchall()

        # Print out the results to demonstrate verification
        print(f"[SUCCESS] Successfully retrieved {len(fetched_records)} records from the database:")
        print("-" * 70)
        print(f"{'ID':<10} | {'Category':<15} | {'Brand':<15} | {'Price ($)':<10}")
        print("-" * 70)
        for row in fetched_records:
            print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<15} | {row[3]:.2f}")
        print("-" * 70)
    except Exception as e:
        print(f"[ERROR] Failed to query database table: {e}")
    finally:
        # Close database connection lifecycle safely
        connection.close()
        print("\n=== Database Connection Safely Closed. User Story Tasks Completed! ===")


if __name__ == "__main__":
    setup_and_query_database()