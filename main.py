import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    colums = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter", colums)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)


    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", colums)
    y_column = st.selectbox("Select Y-axis column", colums)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")
# End of main.py
# I have created a simple data dashboard using Streamlit. The dashboard allows users to upload a CSV file, preview the data, view summary statistics, filter the data based on a selected column and value, and generate a line plot based on selected X and Y columns.