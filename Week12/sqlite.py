import sqlite3

# Connect to database
con = sqlite3.connect("project.db")
cursor = con.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS login_info (
    username TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Take user input
v1 = input("ENTER USERNAME: ")
v2 = input("ENTER EMAIL: ")
v3 = input("ENTER PASSWORD: ")

t = (v1, v2, v3)

# Insert data into table
try:
    cursor.execute(
        "INSERT INTO login_info (username, email, password) VALUES (?, ?, ?)",
        t
    )
    print("DATA INSERTED SUCCESSFULLY!")
except sqlite3.IntegrityError:
    print("ERROR: USERNAME ALREADY EXISTS!")

# Save changes and close connection
con.commit()
con.close()