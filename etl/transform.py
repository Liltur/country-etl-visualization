import pandas as pd
# In the context of the ETL project using the REST Countries API, here are some basic transformations you can apply to the data after extraction and before loading it into the SQLite database:
# Read csv file from raw_data
df = pd.read_csv("./data/raw_data/countries.csv")
print(df.head())

# Display some basic information of dataframe
print(df.info())
print("")
print(df.describe())
print("")

# 1. Data Cleaning
# Remove Duplicates: Ensure that there are no duplicate entries for countries in the dataset.
# Handle Missing Values: Check for any missing values in critical fields (like name, capital, or population) and decide how to handle them (e.g., filling with a default value or dropping those rows).
df.drop_duplicates(subset='name', inplace=True)  # Remove duplicates based on country name
df.fillna("Unknown", inplace=True)  # Fill missing values with "Unknown"

# 2. Data Type Conversion
# Convert Data Types: Ensure that numeric fields such as population and area are of the correct data type (e.g., integers or floats).
df['population'] = df['population'].astype(int)  # Convert population to integer
df['area'] = df['area'].astype(float)  # Convert area to float

# 3. String Manipulations
# Normalize Text: Ensure consistency in text formatting (e.g., capitalizing country names or trimming whitespace).
df['name'] = df['name'].str.strip().str.title()  # Strip whitespace and title case
df['capital'] = df['capital'].str.strip().str.title()  # Normalize capital names

# 4. Creating New Columns
# Calculate Density: You can calculate the population density and create a new column for it.
df['density'] = df['population'] / df['area']  # Population density

# 5. Renaming Columns
# Rename Columns for Clarity: You might want to rename columns for better understanding or consistency.
df.rename(columns={'name': 'country_name', 'capital': 'capital_city'}, inplace=True)  # Rename columns

# 7. Encoding Categorical Data
# Convert Categorical Variables to Numerical: If you plan to perform machine learning, you may want to encode categorical variables.
# python
# countries_df['region'] = countries_df['region'].astype('category').cat.codes  # Convert region to numerical codes

# Summary
# These transformations help ensure that your data is clean, consistent, and in a suitable format for analysis or storage. 
# You can implement these transformations in the "Transform" step of your ETL pipeline, enhancing the quality and usability of the dataset before loading it into the database.
print(f"Final data set after transforming")
print(df.head(10))

# Saving processed_data
df.to_csv("./data/process_data/countries.csv", encoding="utf-8", index=False, errors='ignore')
print(f"Transform successfully.")