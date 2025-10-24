import pandas as pd
import mysql.connector

# Load CSV file
df = pd.read_csv('netflix_titles.csv')

# Clean Data
df = df.dropna(subset=['type', 'title', 'director'])

# fill missing values to avoid errors while inserting
df = df.fillna('')

# Keep only these 11 columns 
columns = [
    'show_id', 'type', 'title', 'director', 'country',
    'date_added', 'release_year', 'rating',
    'duration', 'listed_in', 'description'
]
df = df[columns]

# Connecting to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="230606",  
    database="netflix_db"
)
cursor = conn.cursor()

# Create table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS netflix_titles (
    show_id VARCHAR(20),
    type VARCHAR(10),
    title VARCHAR(255),
    director VARCHAR(255),
    country VARCHAR(255),
    date_added VARCHAR(100),
    release_year INT,
    rating VARCHAR(10),
    duration VARCHAR(20),
    listed_in TEXT,
    description TEXT
)
""")

# Insert Data
insert_query = """
    INSERT INTO netflix_titles (
        show_id, type, title, director, country,
        date_added, release_year, rating,
        duration, listed_in, description
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully!")
