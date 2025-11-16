# Simple Data Dashboard

This project is a lightweight, interactive **data exploration
dashboard** built using **Streamlit**. It allows users to upload a CSV
file, preview the data, view basic statistical summaries, apply filters,
and generate simple line charts --- all from a web-based interface.

## 🚀 Features

### 📂 CSV Upload

-   Upload any CSV file directly through the interface.
-   Automatically loads and displays the first few rows.

### 📊 Data Preview

-   Displays the first 5 rows of the uploaded dataset.

### 📈 Data Summary

-   Generates a statistical summary using `pandas.describe()`.

### 🔎 Data Filtering

-   Select a column and then a specific value from that column.
-   View only the rows matching the selected filter.

### 📉 Data Plotting

-   Choose any column for the X-axis and Y-axis.
-   Generates a line chart using the filtered dataset.

## 🛠️ Technologies Used

-   **Python**
-   **Streamlit**
-   **Pandas**
-   **Matplotlib**

## 📦 Installation

``` bash
pip install streamlit pandas matplotlib
```

## ▶️ Running the App

``` bash
streamlit run app.py
```

## 📜 Example Code

``` python
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
```
