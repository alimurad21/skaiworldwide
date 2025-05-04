import psycopg2

# Database config — update with your actual details
DB_CONFIG = {
    'user': 'postgres',
    'password': 'admin',
    'database': 'postgres',
    'host': 'localhost',
    'port': 5432,
}


# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("Connected to PostgreSQL")

    # --- CREATE TABLE ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            department VARCHAR(50)
        );
    """)
    conn.commit()

    # --- INSERT DATA ---
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s);",
                   ('Alice', 30, 'HR'))
    conn.commit()

    # --- READ DATA ---
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()
    print("\nEmployees Table:")
    for row in rows:
        print(row)

    # --- UPDATE DATA ---
    cursor.execute("UPDATE employees SET age = %s WHERE name = %s;", (31, 'Alice'))
    conn.commit()

    # --- DELETE DATA ---
    # cursor.execute("DELETE FROM employees WHERE name = %s;", ('Alice',))
    # conn.commit()

except Exception as e:
    print("Error:", e)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection closed.")
