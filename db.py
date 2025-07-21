import sqlite3

def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS posts;
        """
    )
    conn.execute(
        """
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    posts_seed_data = [
        ("First Post", "This is the first post"),
        ("Second Post", "This is the second post"),
        ("Third Post", "This is the third post"),
        ("Fourth Post", "This is the fourth post"),
    ]
    conn.executemany(
        """
        INSERT INTO posts (title, content)
        VALUES (?, ?);
        """,
        posts_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()

if __name__ == "__main__":
    initial_setup()