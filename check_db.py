import sqlite3

# Connect to the database
conn = sqlite3.connect('instance/bookings.db')
cursor = conn.cursor()

# Get table schema
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='booking'")
result = cursor.fetchone()

if result:
    print("Current booking table schema:")
    print(result[0])
    
    # Get column information
    cursor.execute("PRAGMA table_info(booking)")
    columns = cursor.fetchall()
    print("\nColumns in booking table:")
    for col in columns:
        print(f"  {col[1]}: {col[2]} (nullable: {not col[3]})")
else:
    print("booking table not found")

conn.close()
