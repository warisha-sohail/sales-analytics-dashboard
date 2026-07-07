import pandas as pd
import os

def extract_data(file_path):
    #Extracts data from the CSV file
    print("Executing Extract Phase...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing raw data file at {file_path}")
    return pd.read_csv(file_path, encoding='windows-1252')

def transform_data(df):
    #Cleans and transforms the data based on available columns
    print("Executing Transform Phase...")
    
    # 1. Drop exact duplicates
    df = df.drop_duplicates()
    
    # 2. Handle Missing Values in Postal Code
    df['Postal Code'] = df['Postal Code'].fillna(0).astype(int)
    
    # 3. Feature Engineering: Calculate Profit Margin
    # Using a lambda function to avoid division by zero if Sales is 0
    df['Profit Margin'] = df.apply(lambda row: (row['Profit'] / row['Sales']) * 100 if row['Sales'] > 0 else 0, axis=1)
    
    # 4. Clean text columns
    text_cols = ['Ship Mode', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'Sub-Category']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            
    return df

def load_data(df, output_path):
    #Loads the cleaned data into a processed CSV directory
    print(f"Executing Load Phase... Saving to {output_path}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print("ETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    RAW_DATA_PATH = "data/raw/superstore_raw.csv"
    PROCESSED_DATA_PATH = "data/processed/superstore_clean.csv"
    
    #Run the pipeline
    raw_df = extract_data(RAW_DATA_PATH)
    clean_df = transform_data(raw_df)
    load_data(clean_df, PROCESSED_DATA_PATH)
