import streamlit as st
import pandas as pd

st.title("Loan Application Report Generator")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV file
    data = pd.read_csv(uploaded_file)

    # Show table
    st.write(data)

    # Show summary statistics
    st.write("Summary statistics:")
    st.write(data.describe())

    # Show a histogram of the data
    st.write("Histogram:")
    st.hist(data)