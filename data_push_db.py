import pandas as pd
import sqlite3

# Connect to SQLite
conn = sqlite3.connect("faculty.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS faculty (
    faculty_id TEXT,
    Name TEXT,
    Education TEXT,
    Research_area TEXT,
    Profile_URL TEXT,
    Email TEXT,
    Contact_Number TEXT,
    Photo TEXT
)
""")

df = pd.read_csv("dau_faculty.csv")


df.to_sql(
    "faculty",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Data pushed successfully .")
