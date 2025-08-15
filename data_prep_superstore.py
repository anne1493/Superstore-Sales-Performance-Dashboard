import pandas as pd

print("Starting data preparation script...")
input_csv_file = 'train.csv'
output_csv_file = 'Store_Sales_Cleaned_for_PowerBI.csv'
try:
    df = pd.read_csv(input_csv_file)
    print(f"'{input_csv_file}' loaded successfully! Original shape: {df.shape}")
    print("First 5 rows of original data:")
    print(df.head())
    print("-" * 30)
except FileNotFoundError:
    print(f"Error: '{input_csv_file}' not found.")
    print("Please make sure the CSV file is in the same directory as this script, or provide the full path.")
    exit()

print("Converting 'Order Date' to datetime format...")
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

print("Filtering data for orders from 2017 onwards...")
df_filtered = df[df['Order Date'].dt.year >= 2017].copy()
print(f"Data filtered. New shape (rows after 2017): {df_filtered.shape}")

print("Selecting final columns...")
df_final = df_filtered[[
    'Row ID',
    'Order ID',
    'Order Date',
    'Ship Date',
    'Ship Mode',
    'Customer ID',
    'Customer Name',
    'Segment',
    'Country',
    'City',
    'State',
    'Postal Code',
    'Region',
    'Product ID',
    'Category',        
    'Sub-Category',    
    'Product Name',
    'Sales' 
]]
print(f"Final data shape after column selection: {df_final.shape}")

print("\nFirst 5 rows of transformed data ready for Power BI:")
print(df_final.head())
print("-" * 30)


print(f"Saving transformed data to '{output_csv_file}'...")
df_final.to_csv(output_csv_file, index=False)

print(f"Data preparation complete! Transformed data saved to: {output_csv_file}")
