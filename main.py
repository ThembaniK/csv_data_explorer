# import streamlit as st
import pandas as pd

# Path to CSV
file_path = "./Free_Test_Data_200KB_CSV-1.csv"

df = pd.read_csv(file_path)

# Display first 5 rows by default
print(df.head())

# Get last 5 riws by default
print(df.tail())

# Get basic info about DataFrame
print("\nDataFrame Info:")
print(df.info())

# Get descriptive statistics
print("\nDataFrame Summary Stats:")
print(df.describe())


# st.title("Interactive CSV Data Explorer")


# Add file uploa widget 
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Process the file if uploaded
# if uploaded_file is not None:
    # Read the CSV file
    # df = pd.read_csv(uploaded_file)

    # Display information about the DataFrame
    # st.subheader("Data Preview (First 5 rows)")
    # st.dataframe(df.head())

    # Continue with other requirements...
# else:
    # st.info("Please upload a CSV file to get started.")