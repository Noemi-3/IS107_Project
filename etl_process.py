import zipfile
import os
import pandas as pd
from sqlalchemy import create_engine

#Zip file path and where to extract it
zip_file_path = r'C:\Users\HP\Downloads\online+retail.zip'
extract_path = r'C:\Users\HP\Downloads\Dataset'

#Unzip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

#After extracting, list the files in the folder
print("Files extracted:", os.listdir(extract_path))

# Load the Excel file into a pandas DataFrame
excel_file_path = os.path.join(extract_path, 'Online Retail.xlsx')
data = pd.read_excel(excel_file_path)

# Preview the data
print(data.head())

# Example: Handling missing values and removing duplicates
data['CustomerID'] = data['CustomerID'].fillna(-1)  # Assign back to the column
data = data.drop_duplicates()  # Assign the result back to data

# Example: Creating a new column for total price
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Preview the transformed data
print(data.head())

# Database connection and loading the DataFrame into PostgreSQL
engine = create_engine('postgresql://postgres:admin@localhost:5432/Online_Retail_DB')

# Load the DataFrame into PostgreSQL
data.to_sql('sales', engine, index=False, if_exists='replace')

print("Data loaded into PostgreSQL successfully.")
