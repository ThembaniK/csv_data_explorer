import streamlit as st
import pandas as pd

# Path to CSV
file_path = "./Free_Test_Data_200KB_CSV-1.csv"

# try:
#     # Load the file with error handling for parsing 
#     df = pd.read_csv(file_path,
#                      on_bad_lines='warn', # Updated from error_bad_lines in newer pandas
#                      na_values=['', 'NA', 'NULL', 'N/A'], # Define values to treat as NaN
#                      low_memory=False) # For mixed data types

#     # Clean the data by removing rows that are all NaN
#     original_row_count = len(df)
#     df_clean = df.dropna(how='all')
#     cleaned_row_count = len(df_clean)

#     if original_row_count != cleaned_row_count:
#         print(f"Note: Removed {original_row_count - cleaned_row_count} empty rows.")

#     # Display first 5 rows by default
#     print("First 5 rows:")
#     print(df_clean.head())

#     # Get last 5 rows by default
#     print(df_clean.tail())

#     # Get basic info about DataFrame
#     print("\nDataFrame Info:")
#     print(df_clean.info())

#     # Get descriptive statistics
#     print("\nDataFrame Summary Stats:")
#     print(df_clean.describe())

# except FileNotFoundError:
#     print(f"Error: file {file_path} not found.")
# except pd.errors.EmptyDataError:
#     print("Error: The CSV file is empty.")
# except pd.errors.ParseError:
#     print("Error: Unable to parse the CSV file. check the file format.")
# except Exception as e:
#     print(f"An unexpected error occured: {str(e)}")


st.title("Interactive CSV Data Explorer")


# Add file upload widget 
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Process the file if uploaded
if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display information about the DataFrame
        st.subheader("Data Preview (First 5 rows)")
        st.dataframe(df.head())
        st.dataframe(df.tail())
        st.dataframe(df.info())
        st.dataframe(df.describe())

        # Continue with other requirements...
else:
        st.info("Please upload a CSV file to get started.")