import streamlit as st
import pandas as pd
import io 
import sys

st.title("Interactive CSV Data Explorer")


# Add file upload widget 
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Process the file if uploaded
if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display information about the DataFrame
        st.subheader("Data Preview (First 5 rows)")
        st.dataframe(df.head())

        # Display the last 5 rows of the dataframe
        st.subheader("Data Preview (Last 5 rows)")
        st.dataframe(df.tail())
        
        # Display the number of rows and columns
        st.subheader("Column Information")
        st.write("Column Names:")
        
        st.write(df.columns.tolist()) # Display column names as a list

        st.write("Data Types:")
        st.dataframe(df.dtypes) # Display data types in a table

        st.subheader("Dataframe Info")
        buffer = io.StringIO()
        sys.stdout = buffer

        try:
             df.info()
        finally:
             sys.stdout = sys.__stdout__

        info_string = buffer.getvalue()
        st.text(info_string)

        st.subheader("Descriptive Statistics")
        st.dataframe(df.describe())

    except Exception as e:
         st.error(f"Error reading or processing the CSV file: {e}")
         st.info("Please ensure the file is a valid CSV format.")

else:
        st.info("Please upload a CSV file to get started.")