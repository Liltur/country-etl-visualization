import pyodbc
import pandas as pd
# create table
# Define your connection parameters
server = 'LAPTOP-QGF8ATS2'
database = 'test'
username = 'your_username'
password = 'your_password'
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"

# Create a connection
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
# Create table if not exists
create_table_query = '''
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[countries]') AND type in (N'U'))
BEGIN
    CREATE TABLE [countries] (
        name NVARCHAR(100),
        capital NVARCHAR(100),
        region NVARCHAR(50),
        subregion NVARCHAR(50),
        population INT,
        area FLOAT,
        languages NVARCHAR(255),
        timezones NVARCHAR(255),
        density FLOAT
    )
END
'''
cursor.execute(create_table_query)
conn.commit()


# Load DataFrame to SQL Server
df = pd.read_csv("./data/process_data/countries.csv")

for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO countries (name, capital, region, subregion, population, area, languages, timezones, density)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', row['country_name'], row['capital_city'], row['region'], row['subregion'], row['population'], row['area'], row['languages'], row['timezones'],row['density'])

conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data has been successfully uploaded to SQL Server.")