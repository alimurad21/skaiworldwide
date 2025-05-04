import psycopg2

# AgensSQL connection config
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin'
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print(" Connected to AgensSQL")

    #  Set graph_path to target graph (if you have one)
    graph_name = 'my_graph'
    cursor.execute(f"SET graph_path = {graph_name};")

    # --- CREATE GRAPH (if not exists) ---
    cursor.execute(f"CREATE GRAPH IF NOT EXISTS {graph_name};")
    conn.commit()
    print(f" Graph `{graph_name}` is ready.")

    # --- CREATE NODE ---
    cursor.execute("""
        SELECT * FROM cypher($$
            CREATE (n:Person {name: 'Alice', age: 30})
            RETURN n
        $$) AS (n agtype);
    """)
    conn.commit()
    print("👤 Node created.")

    # --- MATCH NODE ---
    cursor.execute("""
        SELECT * FROM cypher($$
            MATCH (n:Person)
            RETURN n
        $$) AS (n agtype);
    """)
    rows = cursor.fetchall()
    print("\n Nodes:")
    for row in rows:
        print(row[0])

except Exception as e:
    print("Error:", e)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("AgensSQL connection closed.")
