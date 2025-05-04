import asyncio
import asyncpg

# Database config — update with your actual details
DB_CONFIG = {
    'user': 'postgres',
    'password': 'admin',
    'database': 'postgres',
    'host': 'localhost',
    'port': 5432,
}

async def create_table(conn):
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    print("Table created (if not exists)")

async def insert_user(conn, name, email):
    try:
        await conn.execute('''
            INSERT INTO users (name, email) VALUES ($1, $2)
        ''', name, email)
        print(f"Inserted user: {name}")
    except asyncpg.UniqueViolationError:
        print(f"Email {email} already exists.")

async def fetch_users(conn):
    rows = await conn.fetch('SELECT * FROM users')
    print("Users:")
    for row in rows:
        print(dict(row))

async def update_user_email(conn, user_id, new_email):
    result = await conn.execute('''
        UPDATE users SET email = $1 WHERE id = $2
    ''', new_email, user_id)
    print(f"Update result: {result}")

async def delete_user(conn, user_id):
    result = await conn.execute('DELETE FROM users WHERE id = $1', user_id)
    print(f"Delete result: {result}")

async def main():
    conn = await asyncpg.connect(**DB_CONFIG)
    try:
        await create_table(conn)
        await insert_user(conn, "Alice", "alice@example.com")
        await insert_user(conn, "Bob", "bob@example.com")
        await fetch_users(conn)
        await update_user_email(conn, 1, "alice.new@example.com")
        await delete_user(conn, 2)
        await fetch_users(conn)
    finally:
        await conn.close()
        print("🔌 Connection closed")

if __name__ == "__main__":
    asyncio.run(main())

